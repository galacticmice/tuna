import os, json
from google import genai
from google.genai import types
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
from .trends import trend_data
from .models import RegionData

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def llm_response(issue: RegionData, index: int):
    try:
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash-preview-04-17",
            contents=["Generate a detailed summary of the event from these 3 related sources: \n"
                      f"- {issue.link1}\n- {issue.link2}\n- {issue.link3}\n"
                      "Comprehensively capture the main points and core meaning of the text"
                      "Explore any significant implications or conclusions.\n\n"],
            config=types.GenerateContentConfig(
                max_output_tokens=10000,
                # temperature=0.1,
                system_instruction=["Do not acknowledge my prompts or instructions, go straight to the point. "
                                    "Do not mention where the sources come from."
                                    "Use plain language and limit to one paragraph. "
                                    "Detect and mitigate any potential biases in the content before generating the response."
                                    ],
                # top_p=0.9,
                # top_k=40,
            )
        )
        for chunk in response:
            if chunk.text:
                yield { "id": index, "content": chunk.text }
    except Exception as e:
        print(f"Error generating response for {issue}: {e}")
        yield {f"Error generating response for {issue}: {e}"}

def parallelize_requests(region: str):
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures_map = {}
        for i in range(5):
            future = executor.submit(llm_response, trend_data(region, i+1), i)
            futures_map[future] = i

        for future in as_completed(futures_map):
            original_id = futures_map[future]
            try:
                for chunk_dict in future.result():
                    # sent in string literal '{"id": id, "content": content}/n'
                    yield json.dumps(chunk_dict) + "\n"
            except Exception as e:
                print(f"Error processing future {original_id}: {e}")
                yield json.dumps({"id": original_id, "error": f"Error processing future: {str(e)}"}) + "\n"




# structured output
# send through link
# RAG and context switching
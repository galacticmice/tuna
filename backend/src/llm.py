import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

from .database import add_entry, get_entry
from .trends import trend_data
from .models import RegionData, SummarizedData

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))


def llm_response(issue: RegionData, index: int):
    try:
        if issue is None:
            yield {"id": index, "content": "⚠️ No recent trends found to generate a summary for [category] in [region]."}
            return

        response = client.models.generate_content_stream(
            model="gemini-2.5-flash-preview-04-17",
            contents=["Generate a detailed summary of the event from these 3 related sources: \n"
                      f"- {issue.link1}\n- {issue.link2}\n- {issue.link3}\n"
                      "Comprehensively capture the main points and core meaning of the text."
                      "Explore any significant implications or conclusions.\n\n"],
            config=types.GenerateContentConfig(
                max_output_tokens=10000,
                # temperature=0.1,
                system_instruction=["Do not acknowledge my prompts or instructions, go straight to the point. "
                                    "Do not mention where the sources come from."
                                    "Use plain language and limit to one paragraph. "
                                    "Detect and mitigate any potential biases in the content before generating the response."
                                    "Return response in markdown format to highlight essential ideas of the response."
                                    ],
                # top_p=0.9,
                # top_k=40,
            )
        )
        for chunk in response:
            if chunk.text:
                yield {"id": index, "content": chunk.text}
    except Exception as e:
        print(f"Error generating response for {issue}: {e}")
        yield {"id": index, "error": str(e)}


def parallelize_requests(region: str):
    on_db = get_entry(region)
    if on_db is not None:
        for i in range(5):
            # sent in string literal '{"id": id, "content": content}/n'
            yield json.dumps({"id": i, "content": on_db['summaries'][i]}) + "\n"
    else:
        completed_responses = [""] * 5
        response_had_error = False
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures_map = {}
            for i in range(5):
                future = executor.submit(
                    # WORK HERE!!!!! imported from trends.py
                    llm_response, trend_data(region, i+1, 14), i)
                futures_map[future] = i

            for future in as_completed(futures_map):
                original_id = futures_map[future]
                try:
                    for chunk_dict in future.result():
                        # sent in string literal '{"id": id, "content": content}/n'
                        yield json.dumps(chunk_dict) + "\n"

                        if "content" in chunk_dict and chunk_dict["content"] is not None:
                            completed_responses[original_id] += chunk_dict["content"]
                        elif "error" in chunk_dict:
                            # if error chunk is received, store the error message.
                            # this will overwrite any partial content accumulated for this ID.
                            completed_responses[original_id] = f"Error: {chunk_dict['error']}"
                            response_had_error = True

                except Exception as e:
                    print(f"Error processing future {original_id}: {e}")
                    yield json.dumps({"id": original_id, "error": f"Error processing future: {str(e)}"}) + "\n"
                    completed_responses[original_id] = str(e)
                    response_had_error = True

        # send to DB
        if not response_had_error:
            o = SummarizedData(
                region_code=region,
                summ=[completed_responses[i] for i in range(5)]
            )
            add_entry(o)

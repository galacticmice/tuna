import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

from .models import RegionData

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def llm_response(issue: RegionData):
    response = client.models.generate_content_stream(
        model="gemini-2.5-flash-preview-04-17",
        contents=["Generate a concise summary from these 3 sources: \n"
                f"- {issue.link1}\n- {issue.link2}\n- {issue.link3}\n",
                "Then, generate essential questions that, when answered, "
                "comprehensively capture the contextual meaning and possible implications caused by the event."
                "Answer the questions inquisitively and exploratively.\n\n"],
        config=types.GenerateContentConfig(
            max_output_tokens=2000,
            # temperature=0.1,
            system_instruction=["Maintain a Flesch Reading Ease score of around 65. "
                                "Use plain language and adjust tone dynamically: "
                                "keep it conversational and engaging for general audiences, and more formal or precise for professional topics. "
                                "Use emotional cues sparingly for technical content."
                                "Detect and mitigate any potential biases in the content before generating the response."],
            # top_p=0.9,
            # top_k=40,
        )

    )
    for chunk in response:
        if chunk.text:
            yield chunk.text

# def parallelize_requests(region):
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         futures = {executor.submit()}

# structured output
# send through link
# RAG and context switching
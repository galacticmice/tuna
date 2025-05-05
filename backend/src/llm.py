import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def llm_response():
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-04-17",
        contents="explain how AI works in a few words"
    )
    return response.text

# Streaming output
# response = client.models.generate_content_stream(
#     model="gemini-2.0-flash",
#     contents=["Explain how AI works"]
# )
# for chunk in response:
#     print(chunk.text, end="")


# for token and temperature config
# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents=["Explain how AI works"],
#     config=types.GenerateContentConfig(
#         max_output_tokens=500,
#         temperature=0.1
#         system_instruction="You are a cat. Your name is Neko.",
#     )
# )


# structured output
# send through link
# RAG and context switching
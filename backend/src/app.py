from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import uvicorn
from .llm import llm_response, parallelize_requests

app = FastAPI()

# Global variable for categoryID
categoryID = 0

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/generate')
async def get_llm_response(reg: str, cat: int, lang: str):
    return StreamingResponse(parallelize_requests(reg, cat, lang), media_type="application/x-ndjson")


# Route the HTTP post request to the endpoint /set-category
# @app.post("/set-category")
# # Define set_category with await to allow waiting for a Request object.
# async def set_category(request: Request):
#     global categoryID
#
#     # Declare data variable that will store the received JSON message from the POST request
#     # Notice await is used to keep listening for the request
#     data = await request.json()
#
#     # Declare category variable to grab the categoryID field of the JSON
#     # 0 is the default value if categoryID is blank
#     categoryID = int(data.get("categoryID", 0))
#
#     # Grab language field, defaults to english
#     language = data.get("language", "en")
#
#     # Shown on the backend logs
#     print("Backend received:", categoryID)
#     print("Backend received:", language)
#     # This is shown on the browser console
#     return {"message": f"Received category: {categoryID} Received language: {language}"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import uvicorn
from .llm import llm_response, parallelize_requests

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["get"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/get-llm-response/{country}')
async def get_llm_response(country: str):
    return StreamingResponse(parallelize_requests(country), media_type="application/x-ndjson")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
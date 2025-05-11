from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from typing import Union
import uvicorn

from .llm import llm_response
from .trends import trend_data

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

@app.get("/geo/{geo_id}") # rank?
async def read_item(geo_id: str):
    return {"i_see_the_code": geo_id}

# if want to use query for rank
@app.get("/geo/{geo_id}") # rank?
async def read_item(geo_id: str, q: Union[int, None] = None):
    return {"i_see_the_code": geo_id, "q=?": q}

@app.get('/get-llm-response/{country}')
async def get_llm_response(country: str):
    return StreamingResponse(llm_response(trend_data(country, 1)))


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)

# on click, redirect to /geo_code
# get parameters from url {geo_code} {rank} with urlparser
# use returned parameters to proc db and LLM operation
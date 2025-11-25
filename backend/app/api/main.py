from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess
import os
import sys

app = FastAPI()

class UserPrompt(BaseModel):
    prompt: str
    isVerbose: bool

origins = ["http://localhost:5173"]

abs_wd = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/get_response")
async def get_response(user_prompt: UserPrompt):
    args = [sys.executable, 'main.py']
    if user_prompt.isVerbose == True:
        args.append('--verbose')
    args.append(user_prompt.prompt)

    result = subprocess.run(
            args, 
            cwd=abs_wd, 
            capture_output=True, 
            timeout=30, 
            text=True
        )
    print(result)
    return {"response": result}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Explicit CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["https://your-frontend-url.com"] in production for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    prompt: str

@app.post("/prim3")
async def prim3_endpoint(data: Prompt):
    prompt = data.prompt
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return {"response": completion.choices[0].message.content.strip()}

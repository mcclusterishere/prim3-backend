from fastapi import FastAPI, Request
from openai import OpenAI
import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
import stripe

load_dotenv()

# Load API keys securely from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

# Initialize OpenAI client correctly (new syntax)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize Stripe
stripe.api_key = STRIPE_SECRET_KEY

# Initialize Pinecone correctly
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "prim3-memory"
existing_indexes = pc.list_indexes().names()

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric='euclidean',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

memory_index = pc.Index(index_name)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Prim3 Backend fully running!"}

@app.post("/prim3")
async def prim3_agent(request: Request):
    data = await request.json()
    prompt = data.get("prompt")

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are Prim3 AGI, operational AI agent for Apex Kingdom."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=500
    )

    return {"response": response.choices[0].message.content}

@app.post("/payment")
async def process_payment(request: Request):
    data = await request.json()
    amount = data.get("amount")
    token = data.get("token")

    charge = stripe.Charge.create(
        amount=int(amount * 100),
        currency='usd',
        source=token,
        description='Prim3 AGI Payment'
    )

    return {"status": charge.status, "charge_id": charge.id}

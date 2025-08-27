from fastapi import FastAPI
from app import api1_chat, api2_purchase
from app.db import init_db

app = FastAPI(title="Kuber AI Gold Investment Workflow")

init_db()

app.include_router(api1_chat.router, prefix="/api1", tags=["Chatbot"])
app.include_router(api2_purchase.router, prefix="/api2", tags=["Gold Purchase"])

@app.get("/")
def root():
    return {"message": "Welcome to Kuber AI Gold Investment API. Go to /docs to try it out."}

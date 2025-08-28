from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from app import api1_chat, api2_purchase
from app.db import init_db

app = FastAPI(title="Kuber AI Gold Investment Workflow")

# Initialize the database
init_db()

# Include routers
app.include_router(api1_chat.router, prefix="/api1", tags=["Chatbot"])
app.include_router(api2_purchase.router, prefix="/api2", tags=["Gold Purchase"])

# Replace root with Swagger UI
@app.get("/", include_in_schema=False)
def custom_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Kuber AI Docs")


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.data.model import ChatRequest
from config import get_settings
set = get_settings()

# ==================================================================
# --- Swagger Setting --- 
SWAGGER_HEADERS = {
    "title": "RAG API",
    "version": "0.0.1",
    "description": """RAG API Documents"""
}

app = FastAPI(
    swagger_ui_parameters={
        "deepLinking": True,
        "displayRequestDuration": True,
        "filter": True,
        "syntaxHighlight": {"theme": "default"}
    },
    **SWAGGER_HEADERS
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.post("/chat", tags=["Application"])
def chat(request: ChatRequest):
    return {"message": "Hello, world!"}

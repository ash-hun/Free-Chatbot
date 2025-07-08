from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.data.model import ChatDatamodel
from core.api.inference import ChatModel
from config import get_settings
set = get_settings()

# --- Swagger Setting --- 
SWAGGER_HEADERS = {
    "title": "Sample RAG API for Infra Edu",
    "version": "0.0.1",
    "description": """API Documents"""
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

@app.post("/chat")
def chat(request: ChatDatamodel):
    model = ChatModel()
    response = model.invoke(user_messages=request.user_query)
    return response
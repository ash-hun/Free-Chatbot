from pydantic import BaseModel

class ChatDatamodel(BaseModel):
    user_query: str
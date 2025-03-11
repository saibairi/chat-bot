from pydantic import BaseModel

class ChatBootRequestModel(BaseModel):
    message: str
from .request import Message, ModelName
from uuid import UUID
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: UUID
    status: str
    messages: list[Message]
    model: ModelName
    max_tokens: int
    system_prompt: str | None = None
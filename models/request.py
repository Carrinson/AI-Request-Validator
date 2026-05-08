from enum import Enum
from pydantic import BaseModel, field_validator, Field



class Role(str, Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

class ModelName(str, Enum):
    LLAMA_INSTANT = "llama-3.1-8b-instant"
    LLAMA_VERSATILE = "llama-3.3-70b-versatile"

    CLAUDE_SONNET = "claude-sonnet-4-6"
    CLAUDE_OPUS = "claude-opus-4-7"

    GPT4 = "gpt-4.1"
    GPT5 = "gpt-5.4"


class Message(BaseModel):
    role: Role  
    content: str    

    @field_validator("content")
    @classmethod
    def check_content(cls, content):
        if not content.strip():
            raise ValueError("content cannot be empty")
        else:
            return content
        
class UserRequest(BaseModel):
    messages: list[Message] = Field(min_length=1) 
    model: ModelName
    max_token: int = Field(ge=5, le=500)
    system_prompt: str | None = None
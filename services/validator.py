from models.request import UserRequest
from models.response import UserResponse
from uuid import uuid4

def validate(request: UserRequest):
    uuid = uuid4()

    return UserResponse(
        id= uuid,
        status= "success",
        messages= request.messages,
        model= request.model,
        max_tokens= request.max_tokens,
        system_prompt= request.system_prompt
    )
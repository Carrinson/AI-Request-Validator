from fastapi import APIRouter
from models.request import UserRequest, ModelName
from models.response import UserResponse
from services.validator import validate

router = APIRouter()

@router.post("/validate")
async def validate_request(request: UserRequest):
    return validate(request)
     

@router.get("/models")
async def get_models():
    all_models = [model.value for model in ModelName]
    return all_models
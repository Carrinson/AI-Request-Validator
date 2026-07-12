from fastapi import FastAPI
from routers.validation import router as validation_router

app = FastAPI()

app.include_router(validation_router)

@app.get("/")
async def home():
    return {"message": "Welcome to API Validator"}
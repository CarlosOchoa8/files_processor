from fastapi import APIRouter
from app.endpoints import file_router


api_router = APIRouter()


api_router.include_router(
    router=file_router,
    prefix="/files",
    tags=['files'],
    responses= {418: {"Description": "I'm a teapot =)"}}
)

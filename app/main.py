from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

fastapi_app = FastAPI(
    title= "File processor API.",
    description= "Backend for process and store data from csv/txt file in db.",
    swagger_ui_parameters= {"docExpansion": "None"},
    version="0.0.1",
)

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["GET", "POST"],
    allow_headers = ["*"]
)


@fastapi_app.get("/", status_code=200)
def healthcheck():
    """root healtcheck."""
    return {"Service": "OK"}


app = fastapi_app

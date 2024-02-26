from fastapi import FastAPI
from starlette.exceptions import HTTPException
from core.config import errors
from core.config import routers

def Application() -> FastAPI:

    application = FastAPI(title="Soar API", version="0.0.1")
    application.add_exception_handler(HTTPException, errors.http_error_handler)
    application.include_router(routers.router, prefix="/api")

    return application

app = Application()

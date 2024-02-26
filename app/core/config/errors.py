from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

async def http_error_handler(_: Request, err: HTTPException) -> JSONResponse:

    return JSONResponse({"message": f'{err.status_code} {err.detail}'}, status_code=err.status_code)

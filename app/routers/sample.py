from typing import Union
from fastapi import APIRouter, status, Depends, Request, Form
from fastapi.responses import JSONResponse

#from core.module.test import test1

router = APIRouter()

@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.get("/test/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q, "test":b}

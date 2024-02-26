from fastapi import APIRouter
from routers import sample

router = APIRouter()

router.include_router(sample.router, tags=["sample"])

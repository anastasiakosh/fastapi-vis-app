from fastapi import APIRouter
import math
import time

router = APIRouter(prefix="api", tags=["api"])

@router.get("/wave")
def wave():
    x = list(range(100))
    y = [math.sin(i+time.time()) for i in x]
    return {"x": x, "y": y}

from fastapi import APIRouter
from app.data import generate_data

router = APIRouter(prefix="api", tags=["api"])

@router.get("/wave")
def data():
    return generate_data()
 

from fastapi import APIRouter, Depends
from app.utils.oauth2 import get_current_user

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to the Personal Growth Tracker API!"}

@router.get("/protected")
def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}. This is a protected route!"}

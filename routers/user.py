from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserOut
from controllers.user_controller import register_user
from utils.dependencies import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user(user, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
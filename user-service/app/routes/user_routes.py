from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import *

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users/{id}", response_model=UserResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user
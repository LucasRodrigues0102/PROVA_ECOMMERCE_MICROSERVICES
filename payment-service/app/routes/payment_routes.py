from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.payment_schema import PagamentoCreate, PagamentoResponse
from app.services.payment_service import execute_payment

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/payments", response_model=PagamentoResponse, status_code=status.HTTP_201_CREATED)
def process_payment(pagamento: PagamentoCreate, db: Session = Depends(get_db)):
    return execute_payment(db, pagamento)
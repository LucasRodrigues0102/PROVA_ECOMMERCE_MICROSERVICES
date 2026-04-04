from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.payment_schema import PaymentCreate, PaymentResponse
from app.services.payment_service import process_payment as process_payment_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/payments", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def process_payment(pagamento: PaymentCreate, db: Session = Depends(get_db)):
    return process_payment_service(db, pagamento)
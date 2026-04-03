from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.order_schema import PedidoCreate, PedidoResponse
from app.services.order_service import process_create_order, get_order_by_id

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/orders", response_model=PedidoResponse, status_code=status.HTTP_201_CREATED)
def create_order(order: PedidoCreate, db: Session = Depends(get_db)):
    return process_create_order(db, order)

@router.get("/orders/{id}", response_model=PedidoResponse)
def get_order(id: int, db: Session = Depends(get_db)):
    pedido = get_order_by_id(db, id)
    if not pedido:
         raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido
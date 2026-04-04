from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.inventory_schema import InventoryResponse, InventoryUpdate
from app.services.inventory_service import get_product_inventory, update_product_inventory

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/inventory/{productId}", response_model=InventoryResponse)
def get_inventory(productId: int, db: Session = Depends(get_db)):
    estoque = get_product_inventory(db, productId)
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    return estoque

@router.put("/inventory/{productId}", response_model=InventoryResponse)
def update_inventory(productId: int, update_data: InventoryUpdate, db: Session = Depends(get_db)):
    return update_product_inventory(db, productId, update_data.quantidade)
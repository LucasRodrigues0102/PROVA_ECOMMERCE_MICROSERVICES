from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.services.product_service import *

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/products", response_model=list[ProductResponse])
def list_all(db: Session = Depends(get_db)):
    return get_products(db)

@router.get("/products/{id}", response_model=ProductResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return product
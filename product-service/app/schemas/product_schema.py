from pydantic import BaseModel
from decimal import Decimal

class ProductCreate(BaseModel):
    nome: str
    preco: Decimal

class ProductResponse(ProductCreate):
    ID_Produto: int

    class Config:
        from_attributes = True
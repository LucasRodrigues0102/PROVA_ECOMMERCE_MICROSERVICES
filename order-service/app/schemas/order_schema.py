from pydantic import BaseModel
from typing import List
from decimal import Decimal

class OrderItemCreate(BaseModel):
    id_produto: int
    quantidade: int

class OrderCreate(BaseModel):
    id_usuario: int
    itens: List[OrderItemCreate]

class OrderItemResponse(BaseModel):
    id_produto: int
    produto_nome: str
    preco_unitario: Decimal
    quantidade: int

    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    ID_Pedido: int
    id_usuario: int
    status: str
    total: Decimal
    itens: List[OrderItemResponse]

    class Config:
        from_attributes = True
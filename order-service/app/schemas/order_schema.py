from pydantic import BaseModel
from typing import List
from decimal import Decimal

class ItemPedidoCreate(BaseModel):
    id_produto: int
    quantidade: int

class PedidoCreate(BaseModel):
    id_usuario: int
    itens: List[ItemPedidoCreate]

class ItemPedidoResponse(BaseModel):
    id_produto: int
    produto_nome: str
    preco_unitario: Decimal
    quantidade: int

    class Config:
        from_attributes = True

class PedidoResponse(BaseModel):
    ID_Pedido: int
    id_usuario: int
    status: str
    total: Decimal
    itens: List[ItemPedidoResponse]

    class Config:
        from_attributes = True
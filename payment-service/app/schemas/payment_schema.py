from pydantic import BaseModel
from decimal import Decimal

class PagamentoCreate(BaseModel):
    id_pedido: int
    valor: Decimal

class PagamentoResponse(BaseModel):
    ID_Pagamento: int
    status: str

    class Config:
        from_attributes = True
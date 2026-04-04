from pydantic import BaseModel
from decimal import Decimal

class PaymentCreate(BaseModel):
    id_pedido: int
    valor: Decimal

class PaymentResponse(BaseModel):
    ID_Pagamento: int
    id_pedido: int
    valor: Decimal
    status: str

    class Config:
        from_attributes = True
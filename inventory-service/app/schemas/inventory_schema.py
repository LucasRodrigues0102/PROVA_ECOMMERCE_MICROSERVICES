from pydantic import BaseModel

class InventoryResponse(BaseModel):
    id_produto: int
    quantidade: int

    class Config:
        from_attributes = True

class InventoryUpdate(BaseModel):
    quantidade: int
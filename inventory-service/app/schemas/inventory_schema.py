from pydantic import BaseModel

class EstoqueResponse(BaseModel):
    id_produto: int
    quantidade: int

    class Config:
        from_attributes = True

class EstoqueUpdate(BaseModel):
    quantidade: int
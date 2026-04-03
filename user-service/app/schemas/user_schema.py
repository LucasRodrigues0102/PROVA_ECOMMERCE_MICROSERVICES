from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str

class UserResponse(BaseModel):
    ID_Usuarios: int
    nome: str
    email: str
    senha: str

    class Config:
        from_attributes = True
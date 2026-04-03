from sqlalchemy import Column, Integer
from app.database.connection import Base

class Estoque(Base):
    __tablename__ = "Estoque"

    id_produto = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer, nullable=False, default=0)
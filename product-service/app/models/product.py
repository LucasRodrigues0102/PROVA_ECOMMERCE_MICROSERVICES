from sqlalchemy import Column, Integer, String, DECIMAL
from app.database.connection import Base

class Product(Base):
    __tablename__ = "products"

    ID_Produto = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    preco = Column(DECIMAL(10, 2), nullable=False)
from sqlalchemy import Column, Integer
from app.database.connection import Base

class Inventory(Base):
    __tablename__ = "inventory"

    id_produto = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer, nullable=False, default=0)
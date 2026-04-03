from sqlalchemy import Column, Integer, String, DECIMAL
from app.database.connection import Base

class Pagamento(Base):
    __tablename__ = "Pagamento"

    ID_Pagamento = Column(Integer, primary_key=True, index=True)
    id_pedido = Column(Integer, nullable=False)
    valor = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String(50), nullable=False, default="APROVADO")
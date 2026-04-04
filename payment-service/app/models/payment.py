from sqlalchemy import Column, Integer, DECIMAL, Enum
from app.database.connection import Base

class Payment(Base):
    __tablename__ = "payments"

    ID_Pagamento = Column(Integer, primary_key=True, index=True)
    id_pedido = Column(Integer, nullable=False)
    valor = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Enum("APROVADO", "RECUSADO"), nullable=False)
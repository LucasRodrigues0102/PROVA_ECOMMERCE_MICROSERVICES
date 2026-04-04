from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Order(Base):
    __tablename__ = "orders"

    ID_Pedido = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, nullable=False)
    status = Column(String(50), default="PENDENTE")
    total = Column(DECIMAL(10, 2), nullable=False)

    itens = relationship("OrderItem", back_populates="pedido")


class OrderItem(Base):
    __tablename__ = "order_items"

    ID_itensPedidos = Column(Integer, primary_key=True, index=True)
    id_pedido = Column(Integer, ForeignKey("orders.ID_Pedido"))
    id_produto = Column(Integer, nullable=False)
    produto_nome = Column(String(255), nullable=False)
    preco_unitario = Column(DECIMAL(10, 2), nullable=False)
    quantidade = Column(Integer, nullable=False)

    pedido = relationship("Order", back_populates="itens")
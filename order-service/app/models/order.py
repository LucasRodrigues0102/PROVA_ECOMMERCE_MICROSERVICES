from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Pedido(Base):
    __tablename__ = "Pedidos"

    ID_Pedido = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, nullable=False)
    status = Column(String(50), default="PENDENTE")
    total = Column(DECIMAL(10, 2), nullable=False)

    itens = relationship("ItemPedido", back_populates="pedido")

class ItemPedido(Base):
    __tablename__ = "ItensPedidos"

    ID_itensPedidos = Column(Integer, primary_key=True, index=True)
    id_pedido = Column(Integer, ForeignKey("Pedidos.ID_Pedido"))
    id_produto = Column(Integer, nullable=False)
    produto_nome = Column(String(255), nullable=False)
    preco_unitario = Column(DECIMAL(10, 2), nullable=False)
    quantidade = Column(Integer, nullable=False)

    pedido = relationship("Pedido", back_populates="itens")
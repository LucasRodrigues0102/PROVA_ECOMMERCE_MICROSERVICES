from sqlalchemy.orm import Session
from app.models.inventory import Estoque

def get_product_inventory(db: Session, product_id: int):
    return db.query(Estoque).filter(Estoque.id_produto == product_id).first()

def update_product_inventory(db: Session, product_id: int, quantidade_nova: int):
    estoque = db.query(Estoque).filter(Estoque.id_produto == product_id).first()
    if not estoque:
        estoque = Estoque(id_produto=product_id, quantidade=quantidade_nova)
        db.add(estoque)
    else:
        estoque.quantidade = quantidade_nova
        
    db.commit()
    db.refresh(estoque)
    return estoque
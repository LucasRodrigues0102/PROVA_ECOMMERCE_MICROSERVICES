from sqlalchemy.orm import Session
from app.models.inventory import Inventory

def get_product_inventory(db: Session, product_id: int):
    return db.query(Inventory).filter(Inventory.id_produto == product_id).first()

def update_product_inventory(db: Session, product_id: int, quantidade_nova: int):
    estoque = db.query(Inventory).filter(Inventory.id_produto == product_id).first()
    if not estoque:
        estoque = Inventory(id_produto=product_id, quantidade=quantidade_nova)
        db.add(estoque)
    else:
        estoque.quantidade = quantidade_nova
        
    db.commit()
    db.refresh(estoque)
    return estoque
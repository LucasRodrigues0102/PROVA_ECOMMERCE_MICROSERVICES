from sqlalchemy.orm import Session
from app.models.product import Product

def create_product(db: Session, product_data):
    product = Product(
        nome=product_data.nome,
        preco=product_data.preco
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db: Session):
    return db.query(Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.ID_Produto == product_id).first()
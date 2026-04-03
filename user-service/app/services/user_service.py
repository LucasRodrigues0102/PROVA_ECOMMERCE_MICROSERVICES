from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, user_data):
    user = User(
        nome=user_data.nome,
        email=user_data.email,
        senha=user_data.senha
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.ID_Usuarios == user_id).first()
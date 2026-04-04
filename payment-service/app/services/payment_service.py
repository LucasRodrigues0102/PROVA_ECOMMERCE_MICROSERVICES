from sqlalchemy.orm import Session
from app.models.payment import Payment

def process_payment(db: Session, payment_data):
    # regra simples de simulação
    status = "APROVADO" if payment_data.valor > 0 else "RECUSADO"

    payment = Payment(
        id_pedido=payment_data.id_pedido,
        valor=payment_data.valor,
        status=status
    )

    db.add(payment)
    db.commit()
    db.refresh(payment)

    return payment
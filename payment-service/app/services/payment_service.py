import random
from sqlalchemy.orm import Session
from app.models.payment import Pagamento

def execute_payment(db: Session, pagamento_data):
    id_gerado = random.randint(100000, 999999) 
    
    novo_pagamento = Pagamento(
        ID_Pagamento=id_gerado,
        id_pedido=pagamento_data.id_pedido,
        valor=pagamento_data.valor,
        status="APROVADO" 
    )
    
    db.add(novo_pagamento)
    db.commit()
    db.refresh(novo_pagamento)
    
    return novo_pagamento
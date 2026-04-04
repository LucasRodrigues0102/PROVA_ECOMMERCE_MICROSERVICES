import requests
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.order import Order, OrderItem

# Portas conforme o README (8001 e 8002 já existem. Vamos usar 8004 e 8005)
PRODUCT_SERVICE_URL = "http://localhost:8001"
INVENTORY_SERVICE_URL = "http://localhost:8004"
PAYMENT_SERVICE_URL = "http://localhost:8005"

def process_create_order(db: Session, order_data):
    total_pedido = 0.0
    itens_validados = []

    # 1. Validação via HTTP (Catálogo e Estoque)
    for item in order_data.itens:
        resp_prod = requests.get(f"{PRODUCT_SERVICE_URL}/products/{item.id_produto}")
        if resp_prod.status_code != 200:
            raise HTTPException(status_code=404, detail=f"Produto {item.id_produto} não existe.")
        produto = resp_prod.json()

        resp_inv = requests.get(f"{INVENTORY_SERVICE_URL}/inventory/{item.id_produto}")
        if resp_inv.status_code != 200 or resp_inv.json()["quantidade"] < item.quantidade:
            raise HTTPException(status_code=400, detail=f"Estoque insuficiente para o produto {item.id_produto}.")

        preco_unitario = float(produto["preco"])
        total_pedido += preco_unitario * item.quantidade

        itens_validados.append({
            "id_produto": item.id_produto,
            "produto_nome": produto["nome"],
            "preco_unitario": preco_unitario,
            "quantidade": item.quantidade
        })

    # 2. Salvar Pedido no Banco
    novo_pedido = Order(id_usuario=order_data.id_usuario, status="PROCESSANDO", total=total_pedido)
    db.add(novo_pedido)
    db.flush()

    for item in itens_validados:
        db.add(OrderItem(id_pedido=novo_pedido.ID_Pedido, **item))

    # 3. Baixar Estoque
    for item in order_data.itens:
        qtd_atual = requests.get(f"{INVENTORY_SERVICE_URL}/inventory/{item.id_produto}").json()["quantidade"]
        requests.put(f"{INVENTORY_SERVICE_URL}/inventory/{item.id_produto}", json={"quantidade": qtd_atual - item.quantidade})

    # 4. Processar Pagamento
    resp_pay = requests.post(f"{PAYMENT_SERVICE_URL}/payments", json={
        "id_pedido": novo_pedido.ID_Pedido,
        "valor": total_pedido
    })

    # 5. Atualizar Status
    if resp_pay.status_code == 201 and resp_pay.json()["status"] == "APROVADO":
        novo_pedido.status = "APROVADO"
    else:
        novo_pedido.status = "REJEITADO"

    db.commit()
    db.refresh(novo_pedido)
    return novo_pedido

def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.ID_Pedido == order_id).first()
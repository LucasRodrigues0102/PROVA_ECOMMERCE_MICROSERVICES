# 🛒 E-commerce Microservices (Product + User Service)



Este projeto contém a implementação inicial de uma arquitetura de microsserviços utilizando **FastAPI**, **Python** e **MySQL**.



Atualmente estão disponíveis:



* ✅ Product Service

* ✅ User Service

* ✅ Order Service 

* ✅ Inventory Service

* ✅ Payment Service

---



# ⚙️ Pré-requisitos



Antes de rodar o projeto, você precisa ter instalado:



* Python 3.10+

* MySQL Server

* Git

* (Opcional) VS Code + Thunder Client



---



# 📦 Clonar o repositório



```bash

git clone <LINK_DO_REPOSITORIO>

cd PROVA_ECOMMERCE_MICROSERVICES

```



---



# 🗄️ Configuração do Banco de Dados



Execute o script SQL fornecido no repositório (ex: `database.sql`), ou crie manualmente:



```sql

CREATE DATABASE product_db;

CREATE DATABASE user_db;

CREATE DATABASE db_orders;

CREATE DATABASE db_inventory;

CREATE DATABASE db_payments;



USE product_db;

CREATE TABLE products (

    ID_Produto INT AUTO_INCREMENT PRIMARY KEY,

    nome VARCHAR(100) NOT NULL,

    preco DECIMAL(10,2) NOT NULL

);



USE user_db;

CREATE TABLE users (

    ID_Usuarios INT AUTO_INCREMENT PRIMARY KEY,

    nome VARCHAR(100) NOT NULL,

    email VARCHAR(100) NOT NULL,

    senha VARCHAR(100) NOT NULL

);

```



---



# 🧪 Como rodar os serviços



## 🔹 1. Product Service



Para que o sistema funcione completamente (especialmente a criação de pedidos), todos os 5 serviços devem estar rodando simultaneamente em terminais separados.



O passo a passo base para TODAS as pastas é o mesmo:



```bash

cd nome-do-servico

```



### Criar ambiente virtual



```bash

python -m venv venv

```



### Ativar o ambiente



```bash

venv\Scripts\activate

```



### Instalar dependências



```bash

pip install -r requirements.txt

```



### Criar arquivo `.env`



Crie um arquivo `.env` na raiz do `product-service`:



```env

DATABASE_URL=mysql+pymysql://root:SUA_SENHA@localhost/nome_data_base

```



### Rodar o serviço



```bash

python -m uvicorn app.main:app --reload <PORTA_DO_SERVICO>

```





# 🔌 Portas utilizadas



| Serviço | Porta |

| ------- | -------|

| Product  | 8001  |

| User     | 8002  |

| Order    | 8003  |

| Iventory | 8004  |

| Payment  | 8005  |





---



# 🧠 Observações importantes

Cada microsserviço possui seu próprio banco de dados isolado.



Cada serviço precisa do seu próprio .env.



O diretório venv não deve ser versionado.



Sempre rode pip install -r requirements.txt antes de iniciar.



A biblioteca requests é obrigatória no order-service para realizar as chamadas HTTP.



---



# 🚀 Testes



Você pode testar os endpoints utilizando o Thunder Client (VS Code), Postman ou Swagger UI (/docs).



Para testar o fluxo orquestrado completo, com os 5 terminais rodando, faça as requisições nesta ordem:



1 .Criar Produto: POST http://localhost:8001/products



2. Criar Usuário: POST http://localhost:8002/users



3. Adicionar Estoque: PUT http://localhost:8004/inventory/1 (Enviando { "quantidade": 10 })



4. Fazer o Pedido: POST http://localhost:8003/orders enviando os itens e o ID do usuário. O serviço deduzirá o estoque e aprovará o pagamento automaticamente.

---



# 📌 Status do projeto



* [x] Product Service

* [x] User Service

* [x] Order Service

* [x] Inventory Service

* [x] Payment Service



---



# 👥 Observação final



Projeto acadêmico finalizado para avaliação, contendo o fluxo completo de e-commerce orquestrado via microsserviços com persistência isolada.

# 🛒 E-commerce Microservices (Product + User Service)

Este projeto contém a implementação inicial de uma arquitetura de microsserviços utilizando **FastAPI**, **Python** e **MySQL**.

Atualmente estão disponíveis:

* ✅ Product Service
* ✅ User Service

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

```bash
cd product-service
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
DATABASE_URL=mysql+pymysql://root:SUA_SENHA@localhost/product_db
```

### Rodar o serviço

```bash
python -m uvicorn app.main:app --reload --port 8001
```

Acesse:
👉 [http://localhost:8001/docs](http://localhost:8001/docs)

---

## 🔹 2. User Service

```bash
cd user-service
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

```env
DATABASE_URL=mysql+pymysql://root:SUA_SENHA@localhost/user_db
```

### Rodar o serviço

```bash
python -m uvicorn app.main:app --reload --port 8002
```

Acesse:
👉 [http://localhost:8002/docs](http://localhost:8002/docs)

---

# 🔌 Portas utilizadas

| Serviço | Porta |
| ------- | ----- |
| Product | 8001  |
| User    | 8002  |

---

# 🧠 Observações importantes

* Cada microsserviço possui seu próprio banco de dados
* Cada serviço precisa do seu próprio `.env`
* O diretório `venv` **não deve ser versionado**
* Sempre rode `pip install -r requirements.txt` antes de iniciar

---

# 🚀 Testes

Você pode testar os endpoints utilizando:

* Thunder Client (VS Code)
* Postman
* Swagger UI (`/docs`)

---

# 📌 Status do projeto

* [x] Product Service
* [x] User Service
* [ ] Order Service
* [ ] Inventory Service
* [ ] Payment Service

---

# 👥 Observação final

Este projeto está em desenvolvimento e será expandido com novos microsserviços e integração entre eles.

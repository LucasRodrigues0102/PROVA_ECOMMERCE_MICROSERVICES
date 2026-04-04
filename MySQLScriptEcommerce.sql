CREATE DATABASE product_db;

USE product_db;

CREATE TABLE products (
    ID_Produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

CREATE DATABASE user_db;

USE user_db;

CREATE TABLE users (
    ID_Usuarios INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL
);

CREATE DATABASE inventory_db;

USE inventory_db;

CREATE TABLE inventory (
    id_produto INT PRIMARY KEY,
    quantidade INT NOT NULL
);

CREATE DATABASE payment_db;

USE payment_db;

CREATE TABLE payments (
    ID_Pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    status ENUM('APROVADO', 'RECUSADO') NOT NULL
);

CREATE DATABASE order_db;

USE order_db;

CREATE TABLE orders (
    ID_Pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    status VARCHAR(50) DEFAULT 'PENDENTE',
    total DECIMAL(10,2) NOT NULL
);

CREATE TABLE order_items (
    ID_itensPedidos INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT,
    id_produto INT NOT NULL,
    produto_nome VARCHAR(255) NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES orders(ID_Pedido)
);
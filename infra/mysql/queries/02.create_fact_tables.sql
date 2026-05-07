CREATE DATABASE IF NOT EXISTS fact;

CREATE TABLE IF NOT EXISTS fact.order (
    id_ INT PRIMARY KEY,
    order_id INT,
    create_at DATETIME,
    order_status VARCHAR(50),
    user_id INT,
    product_id INT
);
CREATE DATABASE IF NOT EXISTS dim;

CREATE TABLE IF NOT EXISTS dim.product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(200),
    price INT
);

CREATE TABLE IF NOT EXISTS dim.user (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(200),
    last_name VARCHAR(200),
    city VARCHAR(200),
    active_address VARCHAR(200),
    is_pro BOOL,
    email VARCHAR(200)
);
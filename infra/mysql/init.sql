CREATE TABLE IF NOT EXISTS cicd_test_event_db.banner_view (
  id INT AUTO_INCREMENT PRIMARY KEY,
  event_time DATETIME,
  banner_id INT,
  user_id INT
);


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

CREATE DATABASE IF NOT EXISTS fact;

CREATE TABLE IF NOT EXISTS fact.order (
    id_ INT PRIMARY KEY,
    order_id INT,
    created_at DATETIME,
    order_status VARCHAR(50),
    user_id INT,
    product_id INT
);

GRANT SELECT,INSERT,UPDATE,DELETE ON dim.* TO 'MySQLUser'@'%';
GRANT SELECT,INSERT,UPDATE,DELETE ON fact.* TO 'MySQLUser'@'%';
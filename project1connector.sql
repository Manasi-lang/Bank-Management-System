create database pythonconnectordb;
use pythonconnectordb;
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    user_name VARCHAR(10),
    Password int(10),
    age int(10),
    Address VARCHAR (10),
    phone_no int(10),
    balance FLOAT
);
select * from customers;

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT,
    amount FLOAT
);
select * from transactions
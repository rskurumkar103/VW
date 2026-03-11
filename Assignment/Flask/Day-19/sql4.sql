
CREATE DATABASE IF NOT EXISTS ecommerce;

--Select the Database to Use
USE ecommerce;

-- Create the Orders Table

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount DECIMAL(10, 2)
);

-- Insert Sample Data into the Orders Table

INSERT INTO Orders (order_id, customer_id, product_id, quantity, total_amount) VALUES
(1, 101, 1, 2, 200.00),  
(2, 102, 2, 1, 150.00), 
(3, 101, 3, 3, 300.00),  
(4, 103, 1, 5, 500.00),  
(5, 104, 4, 10, 1000.00), --
(6, 101, 2, 2, 300.00),  
(7, 102, 1, 1, 100.00), 
(8, 101, 4, 7, 700.00),  
(9, 105, 3, 4, 600.00),  
(10, 103, 5, 6, 600.00);  


-- 1. Find the total amount spent by each customer
SELECT customer_id, SUM(total_amount) AS total_spent
FROM Orders
GROUP BY customer_id;

-- 2. Find the number of orders placed by each customer
SELECT customer_id, COUNT(order_id) AS total_orders
FROM Orders
GROUP BY customer_id;

-- 3. Display customers who placed more than 3 orders
SELECT customer_id
FROM Orders
GROUP BY customer_id
HAVING COUNT(order_id) > 3;

-- 4. Find customers whose total spending is greater than 10,000
SELECT customer_id, SUM(total_amount) AS total_spent
FROM Orders
GROUP BY customer_id
HAVING SUM(total_amount) > 10000;

-- 5. Find products whose total quantity sold is greater than 100
SELECT product_id, SUM(quantity) AS total_quantity_sold
FROM Orders
GROUP BY product_id
HAVING SUM(quantity) > 100;
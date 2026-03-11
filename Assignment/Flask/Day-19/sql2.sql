
CREATE DATABASE IF NOT EXISTS retail_company;
USE retail_company;

-- Customers Table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50)
);

-- Products Table
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
);

-- Orders Table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Order_Items Table
CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Insert data into Customers table
INSERT INTO Customers (customer_id, name, city) VALUES
(1, 'RK', 'Pune'),
(2, 'JK', 'Nagar'),
(3, 'SK', 'Mumbai'),
(4, 'AK', 'Pune'),
(5, 'PK', 'Mumbai');

-- Insert data into Products table
INSERT INTO Products (product_id, product_name, price) VALUES
(1, 'Laptop', 1200.00),
(2, 'Smartphone', 800.00),
(3, 'Headphones', 150.00),
(4, 'Keyboard', 100.00),
(5, 'Monitor', 300.00);

-- Insert data into Orders table
INSERT INTO Orders (order_id, customer_id, order_date, total_amount) VALUES
(1, 1, '2022-01-10', 2400.00),
(2, 1, '2022-02-15', 1200.00),
(3, 2, '2022-03-05', 2200.00),
(4, 3, '2022-04-12', 1500.00),
(5, 4, '2022-05-01', 2000.00),
(6, 5, '2022-06-20', 1800.00);

-- Insert data into Order_Items table
INSERT INTO Order_Items (order_item_id, order_id, product_id, quantity) VALUES
(1, 1, 1, 2),
(2, 1, 2, 1),
(3, 2, 3, 2),
(4, 3, 4, 3),
(5, 3, 5, 1),
(6, 4, 1, 1),
(7, 4, 2, 1), 
(8, 5, 3, 2), 
(9, 6, 5, 2); 

-- 1. Find customers who placed more than 3 orders
SELECT c.customer_id, c.name
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
HAVING COUNT(o.order_id) > 3;

-- 2. Find the top 5 customers by total spending
SELECT c.customer_id, c.name, SUM(o.total_amount) AS total_spending
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_spending DESC
LIMIT 5;

-- 3. Display the most ordered product
SELECT p.product_name, SUM(oi.quantity) AS total_quantity
FROM Products p
JOIN Order_Items oi ON p.product_id = oi.product_id
GROUP BY p.product_id
ORDER BY total_quantity DESC
LIMIT 1;

-- 4. Find customers who never placed an order
SELECT c.customer_id, c.name
FROM Customers c
WHERE c.customer_id NOT IN (SELECT DISTINCT customer_id FROM Orders);

-- 5. Calculate the total revenue generated each month
SELECT DATE_FORMAT(o.order_date, '%Y-%m') AS month, SUM(o.total_amount) AS total_revenue
FROM Orders o
GROUP BY month
ORDER BY month;
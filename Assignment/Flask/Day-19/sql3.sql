
CREATE DATABASE IF NOT EXISTS company_data;

USE company_data;

CREATE TABLE Employees1 (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);



INSERT INTO Employees1 (emp_id, emp_name, department, salary) VALUES
(1, 'Alice', 'HR', 50000.00),
(2, 'Bob', 'IT', 80000.00),
(3, 'Charlie', 'Sales', 60000.00),
(4, 'David', 'IT', 75000.00),
(5, 'Eve', 'HR', 52000.00),
(6, 'Frank', 'Sales', 45000.00),
(7, 'Grace', 'HR', 55000.00),
(8, 'Hannah', 'Sales', 70000.00),
(9, 'Ivan', 'IT', 95000.00),
(10, 'Jack', 'Sales', 62000.00);


-- 1. Find Employees1 whose salary is greater than the average salary of all Employees1
SELECT emp_id, emp_name, salary
FROM Employees1
WHERE salary > (SELECT AVG(salary) FROM Employees1);

-- 2. Find Employees1 whose salary is greater than the average salary of their own department
SELECT e.emp_id, e.emp_name, e.salary
FROM Employees1 e
JOIN (
    SELECT department, AVG(salary) AS avg_salary
    FROM Employees1
    GROUP BY department
) dept_avg ON e.department = dept_avg.department
WHERE e.salary > dept_avg.avg_salary;

-- 3. Find Employees1 who earn the highest salary in their department
SELECT e.emp_id, e.emp_name, e.salary
FROM Employees1 e
JOIN (
    SELECT department, MAX(salary) AS max_salary
    FROM Employees1
    GROUP BY department
) dept_max ON e.department = dept_max.department
WHERE e.salary = dept_max.max_salary;

-- 4. Display Employees1 who earn less than the highest salary in the company but more than the average salary
SELECT e.emp_id, e.emp_name, e.salary
FROM Employees1 e
WHERE e.salary > (SELECT AVG(salary) FROM Employees1)
AND e.salary < (SELECT MAX(salary) FROM Employees1);

-- 5. Find departments whose average salary is greater than the company’s average salary
SELECT department
FROM Employees1
GROUP BY department
HAVING AVG(salary) > (SELECT AVG(salary) FROM Employees1);
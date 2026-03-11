CREATE DATABASE Company_data;
use Company_data;
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    joining_date DATE
);

-- Create Projects Table
CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    start_date DATE,
    end_date DATE
);

CREATE TABLE Employee_Project (
    emp_id INT,
    project_id INT,
    hours_worked DECIMAL(10, 2),
    rating DECIMAL(3, 2),
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id),
    PRIMARY KEY (emp_id, project_id)
);

-- Insert data into Employees table
INSERT INTO Employees (emp_id, emp_name, department, salary, joining_date) VALUES
(1, 'RK', 'HR', 50000.00, '2018-03-01'),
(2, 'SK', 'IT', 80000.00, '2017-05-10'),
(3, 'AK', 'Sales', 60000.00, '2019-06-25'),
(4, 'PK', 'IT', 75000.00, '2020-08-14'),
(5, 'GJ', 'HR', 52000.00, '2021-01-10');

INSERT INTO Projects (project_id, project_name, start_date, end_date) VALUES
(1, 'Project Alpha', '2020-01-01', '2020-12-31'),
(2, 'Project Beta', '2021-02-01', '2021-08-31'),
(3, 'Project Gamma', '2021-03-01', '2021-12-31');

INSERT INTO Employee_Project (emp_id, project_id, hours_worked, rating) VALUES
(1, 1, 120.5, 4.2),
(1, 2, 95.0, 4.5),
(2, 1, 200.0, 4.0),
(2, 3, 180.0, 4.7),
(3, 2, 150.0, 4.3),
(4, 1, 220.0, 4.8),
(5, 3, 100.0, 3.9);

-- 1.employees who worked on more than 2 projects
SELECT emp_id, emp_name
FROM Employees
WHERE emp_id IN (
    SELECT emp_id
    FROM Employee_Project
    GROUP BY emp_id
    HAVING COUNT(project_id) > 2
);

-- 2.  employees whose average rating across projects is above 4
SELECT e.emp_id, e.emp_name
FROM Employees e
JOIN Employee_Project ep ON e.emp_id = ep.emp_id
GROUP BY e.emp_id
HAVING AVG(ep.rating) > 4;

-- 3. highest paid employee in each department
SELECT department, emp_id, emp_name, MAX(salary) AS highest_salary
FROM Employees
GROUP BY department;

--   employees who never worked on any project
SELECT emp_id, emp_name
FROM Employees
WHERE emp_id NOT IN (SELECT DISTINCT emp_id FROM Employee_Project);

-- Find the project with the highest total hours worked
SELECT p.project_id, p.project_name, SUM(ep.hours_worked) AS total_hours
FROM Projects p
JOIN Employee_Project ep ON p.project_id = ep.project_id
GROUP BY p.project_id
ORDER BY total_hours DESC
LIMIT 1;
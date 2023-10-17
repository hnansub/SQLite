# 1. import libraiers 

import sqlite3
from sqlite3 import Error



# # ___________________________________________________
# 2. Create function to create new connection:
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("Company's.sqlite")


# # ___________________________________________________
# 3. Create function to excute queries:
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# # ___________________________________________________
# 4. Create queries for creating tables:
# create_employees_table = """
# CREATE TABLE IF NOT EXISTS employees (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   age INTEGER,
#   gender TEXT,
#   nationality TEXT
# );
# """

# create_position_table = """
# CREATE TABLE IF NOT EXISTS position (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   salary INTEGER
# );
# """

# create_department_table = """
# CREATE TABLE IF NOT EXISTS department (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   description TEXT
# );
# """

# create_emplposition_table = """
# CREATE TABLE IF NOT EXISTS emplposition (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   emply_id INTEGER NOT NULL,
#   position_id INTEGER NOT NULL,
#   FOREIGN KEY (emply_id) REFERENCES employees (id),
#   FOREIGN KEY (position_id) REFERENCES position (id)
# );
# """

# create_empldepart_table = """
# CREATE TABLE IF NOT EXISTS empldepart (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   emply_id INTEGER NOT NULL,
#   depart_id INTEGER NOT NULL,
#   FOREIGN KEY (emply_id) REFERENCES employees (id),
#   FOREIGN KEY (depart_id) REFERENCES department (id)
# );
# """

# create_empl_rate_table = """
# CREATE TABLE IF NOT EXISTS empl_rate (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   emply_id INTEGER NOT NULL,
#   rate INTEGER,
#   FOREIGN KEY (emply_id) REFERENCES employees (id)
#   );
# """


# execute_query(connection, create_employees_table)
# execute_query(connection, create_position_table)
# execute_query(connection, create_department_table)
# execute_query(connection, create_emplposition_table)
# execute_query(connection, create_empldepart_table)
# execute_query(connection, create_empl_rate_table)

# ___________________________________________________
# 5. Create INSERT queries:
# create_employees = """
# INSERT INTO
#   employees (name, age, gender, nationality)
# VALUES
#   ('Emily Anderson', 34, 'Female', 'American'),
#   ('Rajesh Kapoor', 42, 'male', 'Indian'),
#   ('Maria Rodriguez', 29, 'female', 'Mexican'),
#   ('James Smith', 45, 'male', 'British'),
#   ('Chloe Martin', 30, 'female', 'French');
# """

# create_position = """
# INSERT INTO
#   position (name, salary)
# VALUES
#   ('Software Engineer', 7200),
#   ('Marketing Manager', 9167),
#   ('Financial Analyst', 6350),
#   ('Penetration Tester', 10250),
#   ('Human Resources Specialist', 5160);
# """

# create_department = """
# INSERT INTO
#   department (name, description)
# VALUES
#   (' Engineering/Development', 'The Engineering or Development department is responsible for designing, developing, and maintaining software applications and systems. Software engineers work on coding, debugging, testing, and ensuring the functionality and performance of software products.'),
#   ('Marketing', 'The Marketing department is in charge of promoting the companys products or services to the target audience. Marketing Managers oversee marketing strategies, campaigns, branding, and market research to attract and retain customers, increase brand awareness, and drive sales.'),
#   ('Finance', 'The Finance department is responsible for managing the companys financial resources, budgets, and investments. Financial Analysts evaluate financial data, create forecasts, analyze trends, and provide insights to support decision-making related to budgeting, investments, and financial planning.'),
#   ('Cybersecurity', 'The Cybersecurity department is focused on protecting the companys digital assets and data from cyber threats. Penetration Testers, also known as Ethical Hackers, are responsible for assessing the security of the organizations systems and networks by attempting to exploit vulnerabilities to identify and fix security weaknesses.'),
#   ('Human Resources (HR)', 'The HR department manages the companys workforce, including recruitment, employee relations, benefits administration, training, and development. Human Resources Specialists handle tasks such as hiring, onboarding, employee performance management, and ensuring compliance with labor laws and company policies.');
# """


# create_emplposition = """
# INSERT INTO
#   emplposition (emply_id, position_id)
# VALUES
#   (1, 1),
#   (2, 2),
#   (3, 3),
#   (4, 4),
#   (5, 5);
# """

# create_empldepart = """
# INSERT INTO
#   empldepart (emply_id, depart_id)
# VALUES
#   (1, 1),
#   (2, 2),
#   (2, 2),
#   (3, 3),
#   (4, 4),
#   (5, 5);
# """

# create_empl_rate = """
# INSERT INTO
#   empl_rate (emply_id, rate)
# VALUES
#   ( 1, 3),
#   ( 2, 3),
#   ( 3, 2),
#   ( 4, 5),
#   ( 5, 4);
# """

# execute_query(connection, create_employees)
# execute_query(connection, create_position)
# execute_query(connection, create_department)
# execute_query(connection, create_emplposition)
# execute_query(connection, create_empldepart)
# execute_query(connection, create_empl_rate)

# ___________________________________________________
#6. Create SELECT queries:

# Basic SELECT Query:

# select_empl_rate = "SELECT emply_id,rate FROM empl_rate"
# empl_rate = execute_read_query(connection, select_empl_rate)
# for rate in empl_rate:
#     print(rate)

# # ___________________________________________________
# SELECT employees who work in the 'Finance' department using 'Where' and 'join' 

# select_finance_employees = """
# SELECT employees.name, department.name AS department
# FROM employees
# JOIN empldepart ON employees.id = empldepart.emply_id
# JOIN department ON empldepart.depart_id = department.id
# WHERE department.name = 'Finance'
# """
# finance_employees = execute_read_query(connection, select_finance_employees)
# for employee in finance_employees:
#     print(employee)

# # ___________________________________________________
# SELECT all employees with their positions and salaries using 'join'

# select_all_employees_positions_salaries = """
# SELECT employees.name, position.name AS position, position.salary
# FROM employees
# JOIN emplposition ON employees.id = emplposition.emply_id
# JOIN position ON emplposition.position_id = position.id
# """
# employees_info = execute_read_query(connection, select_all_employees_positions_salaries)
# for employee in employees_info:
#     print(employee)

# # ___________________________________________________
# Update the salary of an employee with ID 1 to 50

# update_employee_age = """
# UPDATE employees
# SET age = 50  
# WHERE id = 1
# """
# execute_query(connection, update_employee_age)

# # ___________________________________________________
# This is query for check data after update

# select_employee_age = "SELECT * FROM employees where id = 1 AND age = 50"
# employees = execute_read_query(connection, select_employee_age)
# for employee in employees:
#     print(employee)


# # ___________________________________________________
# This is DELETE Query For all table's

# delete_all_employees = "DELETE FROM employees"
# execute_query(connection, delete_all_employees)

# delete_all_positions = "DELETE FROM position"
# execute_query(connection, delete_all_positions)

# delete_all_departments = "DELETE FROM department"
# execute_query(connection, delete_all_departments)

# delete_all_emplpositions = "DELETE FROM emplposition"
# execute_query(connection, delete_all_emplpositions)

# delete_all_empldeparts = "DELETE FROM empldepart"
# execute_query(connection, delete_all_empldeparts)

# delete_all_emplrates = "DELETE FROM empl_rate"
# execute_query(connection, delete_all_emplrates)

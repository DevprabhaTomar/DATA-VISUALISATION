# File Name: employee_records.py

employees = []

n = int(input("Enter number of employees: "))

for i in range(n):
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Salary: "))

    employees.append((emp_id, name, salary))

# Calculate average salary
total_salary = 0

for emp in employees:
    total_salary += emp[2]

average_salary = total_salary / n

print("\nAverage Salary:", average_salary)

print("\nEmployees with salary above average:")

for emp in employees:
    if emp[2] > average_salary:
        print(emp)
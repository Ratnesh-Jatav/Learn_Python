#  Can you change the self-parameter inside a class to something else (say "harry"). Try changing self to "slf" or "harry" and see the effects.

class Employee:
    def __init__(harry, name, position, salary):
        harry.name = name
        harry.position = position
        harry.salary = salary
        print("Constructor called for:")

        print(f"Name: {harry.name}, Position: {harry.position}, Salary: {harry.salary}")
        print("Employee object created successfully.")
emp1 = Employee("John Doe", "Software Engineer", 75000)
emp2 = Employee("Jane Smith", "Data Scientist", 85000)

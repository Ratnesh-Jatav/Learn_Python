class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        print("Constructor called for:")

        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")
        print("Employee object created successfully.")

emp1 = Employee("John Doe", "Software Engineer", 75000)
emp2 = Employee("Jane Smith", "Data Scientist", 85000)
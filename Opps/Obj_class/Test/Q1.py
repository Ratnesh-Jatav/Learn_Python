# Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    def __init__(self, name, age, salary, tech_stack):
        self.name = name
        self.age = age
        self.salary = salary
        self.tech_stack = tech_stack


        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Tech Stack: {', '.join(self.tech_stack)}")
    


prog1 = Programmer("Alice", 30, 90000, ["Python", "JavaScript", "C++"])
prog2 = Programmer("Bob", 28, 85000, ["Java", "Kotlin", "Swift"])
class employee:
   
    name = "John"
    age = 23

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

emp1 = employee()

emp1.display()
emp1 = employee()
emp1.name = "Alice"
emp1.age = 30
emp1.display()
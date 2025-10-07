#Write a class "calculator" capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return self.number ** 0.5
    
calc = Calculator(4)
print(f"Square: {calc.square()}")

print(f"Cube: {calc.cube()}")
print(f"Square Root: {calc.square_root()}")

calc2 = Calculator(9)
print(f"Square: {calc2.square()}")
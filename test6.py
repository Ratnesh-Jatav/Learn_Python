'''
# This test for the lear the function 

# Q1 Write a program using function to find the greatest of Three numbers entered by the user.
a = 1 
b = 2
c = 3
def greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("The greatest number is:", greatest(a, b, c))


# Q2 write a program using function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")


# Q3 Write a program recursion function to calculate the factorial of a number (a non-negative integer).
def sum(n):
    if  n == 1:
        return 1
    return sum(n-1) + n
print(sum(5))


# Q4 Write a pyton funciton to pront first n lines of the following pattern
# ***
# **    
# *

def pattrern(n):
   if(n==0):
       return
   print('*'*n)
   pattrern(n-1)    
pattrern(3) 
'''

# Q5 Write a python program which converts inches to cms.

def inch_to_cms(inch):
    return inch * 2.54
    n =int(input("Enter inches: "))
    print(f"inches is equal to {inch_to_cms(n)}")
    
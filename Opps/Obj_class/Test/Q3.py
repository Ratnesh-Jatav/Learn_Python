#Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = 0. Does this change the class attribute?

class Test:
    a = 10  
obj = Test()
print("Before changing, class attribute a:", Test.a)  # Output: 10
obj.a = 0
print("After changing, class attribute a:", Test.a)  # Output: 10
print("Object attribute a:", obj.a)  # Output: 0

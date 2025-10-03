




def func(a, b):
    calcul = (a*b) + (a/b)
    print(calcul)

def greet(a, b):
    if (a>b):
        print("a is greater than b")

    else:
        print("b is greater than a")

a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))

greet(a, b)
func(a, b)
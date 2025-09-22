
'''
# Print first n natural numbers using while loop
n = int(input("Enter a number :"))
i = 1
while (i<=n):
    print(i)
    i+=1
    

 '''

n = int (input("Enter a number :"))
for i in range (1, n+1):
     print(" "* (n-i), end="")
     print("* "*i, end="")
     print("\n")
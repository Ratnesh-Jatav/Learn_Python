''' voating eligibility program
----------------------------------------------
Name: If_condition.py
a = input("Enter Your Name :")
b = int(input("Enter Your  Age :"))
if (b>=18):
    print(a+" You are eligible for voting")
elif (b<0):
        print(a+" Please Enter valid Age")
else:
    print(a+" You are not eligible for voting")



    -----------------------------------------------
# Marksheet program

marks1 = int(input("Enter Your Marks :"))
marks2 = int(input("Enter Your Marks :"))
marks3 = int(input("Enter Your Marks :"))
total_marks = (marks1 + marks2 + marks3)*100/300
if (total_marks>=40 and marks1>=33 and marks2>=33 and marks3>=33    ):
    print("Congratulations! You are Passed with ",total_marks,"%")
else:
    print("Sorry! You are Failed with ",total_marks,"%")

    -----------------------------------------------



skm1 = "Make a lot of money"
skm2 = "Buy a new car"
skm3 = "Subscribe to my channel"
skm4 = "Get a new job"
message = input("Enter Your Message :")
if ((skm1 in message) or (skm2 in message) or (skm3 in message) or (skm4 in message)):
    print("This is a Spam Message")
else:
        print("This is not a Spam Message")
        '''
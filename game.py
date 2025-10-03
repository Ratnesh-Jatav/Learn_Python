import random
computer = random.choice([-1,0, 1 ])
userstr = input("Enter Your choice: ")
userDict = {"r":-1, "p":0, "s":1}
reverseDict = {-1:"Rock", 0:"Paper", 1:"Scissor"}
user = userDict[userstr]
print(f"You chose {reverseDict[user]}\nComputer chose {reverseDict[computer]}")

if computer == user:
    print("It's a Tie")

else:
    if computer == -1 and user == 1:
        print("You Lose")

    elif computer == -1 and user == 0:
        print("You Win")

    elif computer == 1 and user == -1:
        print("You Win")
        
    elif computer == 1 and user == 0:
        print("You Lose")
    elif computer == 0 and user == -1:
        print("You Lose")
        
    elif computer == 0 and user == 1:
        print("You Win")
    else:
        print("Invalid Input") 
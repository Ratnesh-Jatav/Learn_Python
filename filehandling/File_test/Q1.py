#  Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.

with open("poems.txt") as f:
    content = f.read()
    if "twinkle" in content:
        print("Yes, the word 'twainkle' is present in the file.")
    else:
        print("No, the word 'twainkle' is not present in the file.")
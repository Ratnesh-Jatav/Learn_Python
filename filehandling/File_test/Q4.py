# A file contains a word "Donkey" multiple time you need to replace it with "#######" by updating the same file.

words = ["Donkey", "bad", "ganda"]

with open("Q4.txt", "r") as file:
    content = file.read()

    for word in words:
        content = content.replace(word, "#" * len(word))
    
with open("Q4.txt", "w") as file:
    file.write(content)
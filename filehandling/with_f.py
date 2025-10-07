with open("file0.txt") as f:
    line = f.readline()
    while line != "":
        print(line, end='')  # end='' to avoid double newlines
        line = f.readline()
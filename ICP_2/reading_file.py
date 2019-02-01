fileName = input("Give the name of the file ")
file = open(fileName, 'r+')
for line in file.readlines():
    letters = 0
    words = 0
    for i in line:
        if i.isalpha():
            letters = letters + 1
    print("Number of letters", letters)
    w = line.split()
    words = len(w)
    print("Number of words", words)


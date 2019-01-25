string_input = input("Enter a sentence ")
letters = 0
words = 0
digits = 0
a = string_input.split()
words = len(a)
print("no of words :", words)
for i in string_input:
    if i.isalpha():
        letters = letters + 1
    elif i.isdigit():
        digits = digits + 1
    else:
        words = string_input.count(" ", 1, len(string_input)) + 1

print("Count of letters is :", letters)
print("no of digits is :", digits)
print("no of words :", words)


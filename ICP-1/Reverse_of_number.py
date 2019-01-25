n = int(input("Enter Number"))


def reverse(a):
    rev = 0
    while a > 0:
        rem = a % 10
        rev = rev*10 + rem
        a = a // 10
    return rev


if n < 999:
    n = reverse(n)
    print("Reverse of a number is  :", n)
else:
    print("Enter 3 Digit Number")


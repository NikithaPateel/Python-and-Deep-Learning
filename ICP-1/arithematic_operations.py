while True:
    print("1-addition 2- subtraction  3 - Multiplication 4 - Division")
    c = int(input("enter your option"))

    if c == 1:
        a, b = int(input("enter a ")), int(input("enter b"))
        print("Addition ", a + b)
    elif c == 2:
        a, b = int(input("enter a ")), int(input("enter b"))
        print("Subtraction ", a - b)
    elif c == 3:
        a, b = int(input("enter a ")), int(input("enter b"))
        print("Multiplication ", a * b)
    elif c == 4:
        a, b = int(input("enter a ")), int(input("enter b"))
        print("Division  ", a / b)
    else:
        print("Choose correct choice")









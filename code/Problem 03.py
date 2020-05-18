outputline = "is the biggest number you have entered"
i = 0

while i == 0:
    Num1 = int(input("Enter first number: "))
    Num2 = int(input("Enter second number: "))
    Num3 = int(input("Enter third number: "))
    numbers = [Num1, Num2, Num3]

    if Num1 == "" or Num2 == "" or Num3 == "":
        print("\nError : One or more numbers have no value\n")
        continue

    elif Num1 == Num2 or Num1 == Num3 or Num2 == Num3:
        print("\nError : You have entered two numbers of the same value\n")
        continue

    else:
        for x in numbers:
            if x == Num1:
                if x > Num2 and x > Num3:
                    print(x, outputline)
            elif x == Num2:
                if x > Num1 and x > Num3:
                    print(x, outputline)
            elif x == Num3:
                if x > Num1 and x > Num2:
                    print(x, outputline)
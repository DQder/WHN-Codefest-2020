i = 0

while i == 0:
    print("Enter two different numbers")
    Num1 = input("First number: ")
    Num2 = input("Second number: ")

    if Num1 == "" or Num2 == "":
        print("\nError : You have entered one or more numbers with no value\n")
        continue
    elif Num1 == Num2:
        print("\nError : You have entered two numbers of the same value\n")
    else:
        if Num1 > Num2:
            print(Num1, ">", Num2, "\n")
        else:
            print(Num2, ">", Num1, "\n")
        continue
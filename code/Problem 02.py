i = 0
print("Press 'e' to exit")
while i == 0:
    print("Enter two different numbers")
    # number input
    Num1 = input("First number: ")
    # exit sequence
    if Num1 == "e":
        exit()
    # number input
    Num2 = input("Second number: ")
    # exit sequence
    if Num1 == "e" or Num2 == "e":
        exit()

    # check for errors
    elif Num1 == "" or Num2 == "":
        print("\nError : You have entered one or more numbers with no value\n")
        continue
    elif Num1 == Num2:
        print("\nError : You have entered two numbers of the same value\n")
    # output
    else:
        if Num1 > Num2:
            print(Num1, ">", Num2, "\n")
        else:
            print(Num2, ">", Num1, "\n")
        continue
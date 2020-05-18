i = 0
while i == 0:
    x = input("Enter a number: ")

    if type(x) == str:
        print("Error : You have entered a string instead of a number")
        continue
    elif x < 0:
        print("Your number is a negative number.\n")
    if x == 0:
        print("Your number is equal to zero.\n")
    else:
        print("Your number is a positive number\n")
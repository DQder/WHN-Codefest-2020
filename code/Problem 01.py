i = 0


def subtractreturn():
    Answer = Num1 - Num2
    return Answer


while i == 0:
    Num1 = float(input("Enter your first number: "))
    Num2 = float(input("Enter your second number: "))

    if subtractreturn() % 1 == 0:
        # number is whole
        print(int(subtractreturn()))
    else:
        # number is a fraction
        print(float(subtractreturn()))
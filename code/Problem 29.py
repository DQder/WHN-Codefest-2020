num1 = float(input("Enter your calculation:\n"))
calc = str(input())
num2 = float(input())
numList = [0, 0, 0]


def add():
    print(num1 + num2)


def subtract():
    print(num1 - num2)


def multiply():
    print(num1 * num2)


def divide():
    print(num1 / num2)


if calc == "+":
    add()
elif calc == "-":
    subtract()
elif calc == "*":
    multiply()
elif calc == "/":
    divide()
else:
    print("Error : That is not an available operation")



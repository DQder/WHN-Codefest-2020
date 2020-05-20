def dortIslem():
    num1 = float(input("Enter a number: "))
    calc = input("Enter the symbol: ")
    num2 = float(input("Enter another number: "))

    dic = {
        "+": "addition",
        "-": "subtraction",
        "*": "multiplication",
        "/": "division"
    }
    y = dic.get(calc, "Error : Nut a valid calculation!")
    if y == "addition":
        return num1 + num2
    elif y == "subtraction":
        return num1 - num2
    elif y == "multiplication":
        return num1 * num2
    elif y == "division":
        return num1 / num2


print(dortIslem())
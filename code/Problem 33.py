import math

a = float(input("Enter the first corner length: "))
b = float(input("Enter the second corner length: "))
c = float(input("Enter the third corner length: "))
sideLen = [a, b, c]


def CA():
    print("The circumference of your triangle is", (a + b + c))
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("The area of your triangle is", area)


if abs(b - c) < a < (b + c):
    print("Your triangle is drawable.")
    if a == b == c:
        print("Your triangle is a equilateral triangle.")
        CA()
    elif a == b or a == c or b == c:
        print("Your triangle is a isosceles triangle")
        CA()
    else:
        print("Your triangle is a scalene triangle")
        CA()

else:
    print("Your triangle is not drawable.")
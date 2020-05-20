a = float(input("Enter the first corner length: "))
b = float(input("Enter the second corner length: "))
c = float(input("Enter the third corner length: "))

if abs(b - c) < a < (b + c):
    print("Your triangle is drawable.")

else:
    print("Your triangle is not drawable.")
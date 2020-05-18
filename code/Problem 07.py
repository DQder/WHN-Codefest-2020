x = float(input("Enter a number: "))

if x % 1 != 0:
    print("Error : Girdipiniz sayı kesirlidir.")

elif x % 2 == 0:
    print("Girdiğiniz sayı çift sayıdır.")
else:
    print("Girdiğiniz sayı tek sayıdır.")
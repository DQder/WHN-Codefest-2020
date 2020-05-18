price = float(input("Enter the price of the product: "))
taxRate = float(input("Enter the tax rate (your tax rate can be lower than 0 to represent a discount: "))

finalPrice = (price * (taxRate + 100))/100
print("It will cost you", str(finalPrice) + "₺")
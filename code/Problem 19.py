T = float(input("Enter the heat (celsius) of the water: "))

if T < 0:
    print("The water is in solid form")
elif 0 < T < 100:
    print("The water is in liquid form")
elif T > 100:
    print("The water is in gas form")
elif T == 0:
    print("The waters form is in between solid and liquid")
elif T == 100:
    print("The waters form is in between liquid and gas")
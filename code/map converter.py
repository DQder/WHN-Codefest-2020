i = 0
while i == 0:
    mapDistance = input("Enter the distance calculated on the small map: ")
    if mapDistance == "x":
        break
    print("The length on the real map is:", (29.5 * float(mapDistance)) / 9.5)
exit()
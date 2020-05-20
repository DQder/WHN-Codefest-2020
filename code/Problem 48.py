loop = 0


def switcher(value):
    monthDic = {
        1: "\nOcak\n",
        2: "\nŞubat\n",
        3: "\nMart\n",
        4: "\nNisan\n",
        5: "\nMayıs\n",
        6: "\nHaziran\n",
        7: "\nTemmuz\n",
        8: "\nAğustos\n",
        9: "\nEylül\n",
        10: "\nEkim\n",
        11: "\nKasım\n",
        12: "\nAralık\n"
    }
    print(monthDic.get(value, "Month not found!"))


while loop == 0:
    x = float(input("Enter the month number: "))
    switcher(x)
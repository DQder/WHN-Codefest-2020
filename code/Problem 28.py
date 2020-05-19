NumList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while i < 10:
    a = float(input("Enter a number: "))
    NumList[i] = a
    i += 1

avList = sum(NumList) / len(NumList)
avLS = (max(NumList) + min(NumList)) / 2

print(abs(avList - avLS))
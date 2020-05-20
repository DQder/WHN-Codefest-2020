# saat başına maaş
SaMik = 10
x = float(input("Enter the number of hours you have worked for: "))

if x <= 40:
    print("Maaşınız:", SaMik * x)
elif x > 40:
    extra = (x - 40) / 2
    print("Maaşınız:", SaMik * (40 + extra))
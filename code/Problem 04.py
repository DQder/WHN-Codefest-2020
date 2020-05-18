i = 1
ans = 0
loop = 0

while i < 24:
    i += 2
    if i > 24:
        print("toplam: ", ans)
    else:
        ans += i
    loop += 1
print("ortalama: ", int(ans/(loop-1)))
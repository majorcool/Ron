num = 0
m = int(input("数字"))
n = int(input("项数"))
for a in range(0,n):
    b = "1" * (n - a)
    b = int(b)
    num += b * m
    if a == n - 1:
        print(num)
        break
    a += 1


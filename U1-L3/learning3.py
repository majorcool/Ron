# 打印五遍hellow
i = 0
while i < 5:  # <=4
    print("Hello")
    i += 1
print("循环结束后，i=%d" % i)

a = 0
while a < 10:
    if a == 3:
        break
    print(a)
    a += 1
print("over")
print("循环结束后，a=%d" % a)

b = 0
while b < 10:
    if b == 3:
        b += 1
        continue
    print(b)
    b += 1

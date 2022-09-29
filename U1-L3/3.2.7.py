# 3.1.7 计算 1+2+3+……+100 的值
b = 0
for a in range(1,101):
    b += a
    a += 1
print(b)
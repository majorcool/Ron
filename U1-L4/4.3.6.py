# 4.3.6 改写 #4.2.6：函数内打印乘法表，同时，将打印的算式条数作为函数的返回值。例如完整的乘法表，应有 9+8+7+……+1 共 45 条算式。用任意的方式
# 调用函数，打印乘法表的同时，在下方打印算式条数

def num_99(n):
    over = ""
    mm = 0
    for a in range(1,n+1):
        over += "\n"
        for b in range(1,a+1):
            num = a * b
            a = str(a)
            b = str(b)
            num = str(num)
            over += a + " * " + b + " = " + num + "\t"
            a = int(a)
            b = int(b)
            num = int(num)
    for m in range(1,n+1):
        mm += m
    mm = str(mm)
    over += "\n"
    over += mm
    return over
number = int(input("数字"))
print(num_99(number))
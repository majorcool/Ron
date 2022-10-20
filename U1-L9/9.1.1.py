def factorial(num):  # 递归阶乘
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(1))
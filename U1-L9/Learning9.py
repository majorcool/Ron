def factorial(num):  # 递归阶乘
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(1))


def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)


print(fibonacci(1))

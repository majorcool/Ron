def factorial(num):  # 递归阶乘
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(1))


def fibonacci(num):  # 斐波那契数
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)


print(fibonacci(1))


def han(n):  # 汉诺塔游戏
    if n == 1:
        return 1
    return han(n-1) + 1 + han(n-1)


print(han(10))
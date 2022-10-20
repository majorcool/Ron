def han(n):  # 汉诺塔游戏
    if n == 1:
        return 1
    return han(n-1) + 1 + han(n-1)


print(han(9))
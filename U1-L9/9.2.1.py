def PA(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return PA(n-1) + PA(n-2)


print(PA(2))

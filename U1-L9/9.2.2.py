def dao(n):
    n = str(n)
    if len(n) == 1:
        return n
    else:
        return dao(n[1:]) + n[0]


print(dao(1234567890))
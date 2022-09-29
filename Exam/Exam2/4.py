#修改
for a in range(1,9):
    for b in range(0,9):
        for c in range(0,9):
            if a ** 3+ b ** 3 + c ** 3 == 100 * a + 10 * b + c:
                print(100 * a + 10 * b + c)


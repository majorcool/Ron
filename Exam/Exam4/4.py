def add(num_1, num_2):
    num_1, num_2 = str(num_1), str(num_2)
    n1 = len(num_1.partition(".")[2])
    n2 = len(num_2.partition(".")[2])
    n = max(n1, n2)
    num_1 = num_1.replace(".", "") + ("0" * (n - n1))
    num_2 = num_2.replace(".", "") + ("0" * (n - n2))
    num_final = str(int(num_1) + int(num_2))
    if n > 0:
        num_final = num_final[:-n] + "." + num_final[-n:]
    return num_final


print(add(99999999999999999.999999999999, -0.99999999999999999))
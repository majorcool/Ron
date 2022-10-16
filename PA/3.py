def different(n, str="123456789"):
    long = len(str)
    num = ""
    num_0 = str
    for time in range(0, long, n):
        num_0 = num_0[time:time+n]
        num_0 = num_0[-1:-len(num_0)-1:-1]
        num += num_0
        num_0 = str
    return num


print(different(2))



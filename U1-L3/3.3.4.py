# 3.3.4 用户输入 1 个整数，打印出这个整数的所有因数。打印后程序持续运行，而非结束
z = 1
while z == 1:
    a = int(input("请输入正整数"))
    print(a,end="它的因数有")
    for b in range(1,a+1):
        if a % b == 0:
            print(b, end=",")
    print()
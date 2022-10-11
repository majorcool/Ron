# 3.1.10 分解质因数：用户输入一个正整数，用程序进行分解质因数，如输出 30 = 2 * 3 * 5
num = int(input("请输入数字:"))
print(num, end="=")
a = 2
while num != 1 and num != 0:
    while num % a == 0:
        if num > a:
            num = num / a
            print(" %d" % a, end=" *")
        if num == a:
            num = num / a
            print(" %d" % a)
        if num == 1:
            break
    a += 1
if num <= 0:
    print(" 0")

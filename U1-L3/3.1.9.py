# 3.1.9 质数判断：用户输入一个正整数，用程序判断是否为质数
num = int(input("请输入一个正整数"))
c = 1
while c < num:
    c += 1
    s = num % c
    if s == 0 :
        print("不是质数")
        break
if c == num:
    print("是质数")
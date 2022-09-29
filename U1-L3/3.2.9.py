# 3.1.9 质数判断：用户输入一个正整数，用程序判断是否为质数
num = int(input("请输入一个正整数"))
for a in range(2,num):
    if num % a == 0:
        print("非质数")
        break
if a == num-1:
    print("质数")
if num == 1:
    print("非质数")

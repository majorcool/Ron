# 3.2.10 分解质因数：用户输入一个正整数，用程序进行分解质因数，如输出 30 = 2 * 3 * 5
num = int(input("请输入数字:"))
print(num,end=" = ")
while num > 1:
    for a in range(2,num+1):
        if num % a == 0:
            num = num / a
            num = int(num)
            if num == 1:
                print(a)
                break
            else:
                print(a, end=" * ")
                break


# 3.3.5 有 1 2 3 4 四个数字，组成互不相同且无重复数字的 3 位数，打印出所有结果
count = 0
for num1 in range(1,5):
    for num2 in range(1,5):
        for num3 in range(1,5):
            if num1 == num2 or num2 == num3 or num1 == num3:
                continue
            print(str(num1)+str(num2)+str(num3),end=" ")
            count += 1
print("有%d个"%count)


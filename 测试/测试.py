P = 0
for num in range(1,31):
    grades = int(input("请输入成绩"))
    if grades > 100 or grades < 0:
        print("分数有误请重新输入")
        continue
    P += grades
PJ = float(P / 30)
print(PJ)
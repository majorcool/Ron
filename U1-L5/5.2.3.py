# 5.2.3 将 5.2.2 的函数复制过来，将返回值修改为一个元祖，这个元祖保存了所有学生的成绩
# 在函数外部调用函数，获取所有学生的成绩，打印出所有学生的成绩
# 在函数外部计算所有学生的平均分，打印一条消息显示平均分
def grades():
    list0 = []
    tuple0 = (1)
    grade = 0
    num = 1
    n = int(input("学生数量"))
    while num <= n:
        g = float(input("请输入成绩"))
        if g < 0 or g > 100:
            print("输入错误")
            continue
        num += 1
        list0.append(g)
    k=tuple(list0)
    return k
grades_all = 0
ave = grades()
print(ave)
student_number = len(ave)
for i in range(0, len(ave)):
    grades_all += ave[i]
grades_P = float(grades_all/len(ave))
print(grades_P)








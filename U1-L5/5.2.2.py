# 5.2.2 编写一个函数，功能是计算学生的平均分
# 用户先输入正整数 n，告知学生数量
# 用户输入每个学生的成绩，如果成绩在 0-100 以外，提示用户输入错误
# 学生成绩录入完毕后，计算平均分，将平均分作为返回值
# 在函数外部调用函数，打印出学生的平均分
def grades():
    grade = 0
    num = 1
    n = int(input("学生数量"))
    while num <= n:
        g = float(input("请输入成绩"))
        if g < 0 or g > 100:
            print("输入错误")
            continue
        grade += g
        num += 1
    gradess = grade / n
    return gradess
print(grades())



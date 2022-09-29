# 5.2.9 编写一个函数，功能是计算单人跳水比赛中的一次得分
# 单人项目跳水比赛时由 7 名裁判员分坐在跳台两侧的池岸上评分，最高 10 分，失败 0 分。
# 在计算分数时，去掉 2 个最高分和 2 个最低分，将 3 个中间分数相加之和，乘以动作的难度系数，就是动作的最终得分
grade1 = int(input("第1个分数"))
grade2 = int(input("第2个分数"))
grade3 = int(input("第3个分数"))
grade4 = int(input("第4个分数"))
grade5 = int(input("第5个分数"))
grade6 = int(input("第6个分数"))
grade7 = int(input("第7个分数"))
dif = int(input("难度系数"))
def swim():
    swim_grade = [grade1, grade2, grade3, grade4, grade5, grade6, grade7]
    swim_grade.sort()
    del swim_grade[0]
    del swim_grade[1]
    swim_grade.sort(reverse=True)
    del swim_grade[0]
    del swim_grade[1]
    number = (swim_grade[0] + swim_grade[1] + swim_grade[2]) * dif
    return number
number0 = swim()
print("最终得分为%d"%number0)

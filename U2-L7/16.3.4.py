# 16.3.4  调整列表元素顺序
# 定义一个函数，参数为一个长度为 2n 的列表 [x1,x2,...,xn,y1,y2,...,yn]
# 调整顺序为 [x1,y1,x2,y2,...,xn,yn]，并返回调整后的列表
def two(list_1):
    list_0 = []
    for a in range(0, int(len(list_1)/2)):
        list_0.append(list_1[a])
        list_0.append(list_1[a+int(len(list_1)/2)])
    return list_0


list_2 = [2, 5, 1, 3, 4, 7]
print(two(list_2))








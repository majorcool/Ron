# 5.1.6 定义一个函数，将列表每隔一个元素就增加一个 0，将新列表作为返回值
list_1 = [1,2,3,4,5,6,7]
def add_0():
    b = 0
    for n in range(1,13,+2):
        b = n
        list_1.insert(b,0)
    return list_1
add_0()
print(list_1)
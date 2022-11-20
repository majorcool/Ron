# 16.3.3  找到重复元素
# 定义一个函数，参数为一个长度为 2n 的列表，其中包含 n+1 个不同的元素，只有 1 个元素重复了 n 次；返回重复了 n 次的元素
def num(list_0):
    for a in range(0, len(list_0)):
        for b in range(a+1, len(list_0)):
            if list_0[a] == list_0[b]:
                return list_0[a]


list_1 = [1, 2, 3, 3]
print(num(list_1))



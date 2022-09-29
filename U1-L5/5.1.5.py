# 5.1.5 定义一个函数，作用是将列表中的数字元素全部扩大两倍，其他类型保持不变，修改完成后，将新列表作为返回值
list_num = [66,"S",1]
def xk():
    c = len(list_num)
    b = 0
    while b < c:
        if isinstance(list_num[b], int):
            num = list_num[b] * 2
            list_num[b] = num
        b += 1
    return list_num
n = xk()
print(n)
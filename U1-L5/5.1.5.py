# 5.1.5 定义一个函数，作用是将列表中的数字元素全部扩大两倍，其他类型保持不变，修改完成后，将新列表作为返回值


def xk(list_num):
    long = len(list_num)
    number = 0
    while number < long:
        if type(list_num[number]) == int:
            num = list_num[number] * 2
            list_num[number] = num
        if type(list_num[number]) == float:
            num = list_num[number] * 2
            list_num[number] = num
        number += 1
    return list_num


n = [66, "S", 1.2]
print(xk(n))
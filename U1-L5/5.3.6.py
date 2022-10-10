# 5.3.6 编写一个函数 compare_dict(dict1, dict2)，判断两个字典中存在多少个完全相同的键值对，将重复键值对的数量和重复的键值对保存在一个元祖中
# ，将这个元祖作为返回值
def compare_dict(dict1, dict2):
    empty = []
    num = 0
    empty.append(num)
    for key in dict1:
        one = dict1[key]
        for value in dict2.values():
            two = value
            if one == two:
                empty.append(dict1[key])
                num += 1
                empty[0]=num
    empty = tuple(empty)
    return empty


dict_11 = {1: 2, 2: 3, 3: 4}
dict_22 = {1: 2, 3: 4, 5: 6}
print(compare_dict(dict_11, dict_22))

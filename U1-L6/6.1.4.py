# 6.1.4 定义一个函数，参数为 2 个字符串，从第 1 个字符串中删除第 2 个字符串中所有的字符，返回新的字符串
# 例如，参数为 'They are students.' 和 'aeiou'，返回 'Thy r stdnts.'
def cut(first, cutting):
    long = len(cutting) - 1
    long_1 = len(first) - 1
    for time in range(0, long):
        for a in range(0,long_1):
            if first[time] == cutting[a]:
                first[time] = cutting[a]
    print(first)


cut('They are students.', 'aeiou')

# 不理解
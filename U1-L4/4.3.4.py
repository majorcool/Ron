# 4.2.4 编写一个名为 describe_city() 的函数，它接受 1 座城市的名字以及该城市所属的国家。这个函数应打印 1 个简单的句子，如 "Beijing is in
# China"。给用于存储国家的形参指定默认值。为 3 座不同的城市调用这个函数，且其中至少有 1 座城市不属于默认国家
# 4.3.4 改写 #4.2.4：函数内不打印消息，如果输入的城市和国家匹配，将返回值设置为 'YES'；如果不匹配，将返回值设置为 'NO'。调用 3 次函数，
# 传入不同的参数，输出不同的结果。并且，使用 2 种调用的方式
def describe_city(m,g="China"):
    if m == "beijing" and g == "China":
        return "Yes"
    if m == "shanghai" and g == "China":
        return "Yes"
    if m == "J" and g == "China":
        return "No"
print(describe_city("beijing"))
n = describe_city("shanghai")
print(n)
print(describe_city("J"))
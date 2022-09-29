# 4.2.3 修改 #4.2.2 中的函数 make_shirt()，使其在默认情况下制作一件印有 "I love Python" 的短袖。调用这个函数 3 次，分别制作 1 件大号短袖，
# 印有 "I love Python"；1 件中号短袖，印有 "I love Python"；1 件小号短袖，印有任意其它文字
# 4.3.3 改写 #4.2.3：函数内不打印消息，将消息作为函数的返回值。调用 3 次函数，分别传入不同的参数，打印出不同的消息。并且，使用 2 种调用的方式
def make_shirt(c,z="I love Python"):
    return "尺码为%s，文字为%s"%(c,z)
a = "大"
b = "中"
c = "小"
d = "？？？？？"
print(make_shirt(a))
print(make_shirt(b))
print(make_shirt(c,d))
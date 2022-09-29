# 5.2.4 定义一个元祖类型的购物车，用户可以不断的输入想添加的商品，输入 'q' 结束，打印出当前购物车中商品的数量，以及所有的商品
thing = 0
list0 = []
while True:
    thing = str(input("请输入商品:"))
    if thing == "q":
        break
    list0.append(thing)
print(len(list0))
print(list0)

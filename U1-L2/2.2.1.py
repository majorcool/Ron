has_ticket = int(input("请问您是否有车票？有请输入1，无请输入2："))
if has_ticket == 1:
    print("您有车票，可以进行安检了！")
    knife_length = int(input("所以你身上的刀有几厘米长："))
    if knife_length >= 20:
        print("不能携带超过20厘米的刀上车，您的刀长度为%d厘米" % knife_length)
    else:
        print("安检通过，祝您旅途愉快！")
else:
    print("大哥，先买票，好不？")


has_ticket = int(input("请问您是否有车票？有请输入1，无请输入2："))
knife_length = int(input("您身上的刀几厘米："))
if has_ticket == 1 and knife_length <= 20:
    print("您有车票，刀的长度通过安检，祝您旅途愉快！")
elif knife_length > 20:
    print("不能携带超过20厘米的刀上车，您的刀长度为%d厘米" % knife_length)
elif has_ticket == 2:
    print("大哥，您要先买票啊")





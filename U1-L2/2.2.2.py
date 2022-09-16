your_temperature = int(input("您的体温是："))
if your_temperature <= 37.2:
    your_hesuan_time = int(input("你核酸多少天了："))
    if your_hesuan_time > 3:
        print("请去做核酸")
    else:
        print("欢迎进入校园！")
else:
    print("建议您回家隔离")

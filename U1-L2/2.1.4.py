number = int(input("Please write one number , from 1 to 100:"))
if number == 66:
    print("猜对了！你真聪明！")
elif 66 > number >= 1:
    print("哎呦~猜小了，正确答案是66")
elif 100 >= number > 66:
    print("哎呦~猜大了，正确答案是66")
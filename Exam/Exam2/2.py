b = 1
while b == 1:
    s = str(input("请选择运算方式+-*/"))
    if s == "+":
        num1 = float(input("数字1"))
        num2 = float(input("数字2"))
        jia = num1 - num2
        print(jia)
    elif s == "-":
        num3 = float(input("数字1"))
        num4 = float(input("数字2"))
        jian = num3 - num4
        print(jian)
    elif s == "*":
        num5 = float(input("数字1"))
        num6 = float(input("数字2"))
        cheng = num5 - num6
        print(cheng)
    elif s == "/":
        num7 = float(input("数字1"))
        num8 = float(input("数字2"))
        if num8 == 0:
            print("被除数不为0")
            continue
        chu = num7 - num8
        print(chu)

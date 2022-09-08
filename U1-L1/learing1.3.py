#输出变量
password = input("请输入银行密码")
print(password)
age = input("年龄")
print(age)

print(int(12.1))#int转化整数

print(float(12.2))#print转化小数

#买苹果
#输入苹果单价
pricea = input("苹果的单价")
#输入苹果的重量
weighta = input("苹果的重量")
#计算支付的总金额,两个字符串间不能直接做乘法
#将价格转换成小数
price = float(pricea)
#将重量转化为小数
weight = float(weighta)
#计算金额
money = price * weight
print(money)

#买苹果改进版--------改进内容：将float小数函数提到input输入函数前，节省变量只定义了3个变量
#输入苹果单价
priceb = float(input("苹果的单价"))
#输入苹果重量
weightb = float(input("苹果的重量"))
#计算金额
moneyb = priceb * weightb
print(moneyb)

#格式化输出1，%s字符串
name = "大明"
print("我的名字叫%s，请多多关照！" %name)
#格式化输出2，%d整数,%06d的意思是000000+student_number
student_number = 654
print("我的学号是%06d" %student_number)
#格式化输出3，%f小数,%.2f的意思是小数点后2位
pricec = 8.5
weightc = 7.5
moneyc = pricec * weightc
print("苹果单价%.2f元/斤，买了%.2f斤，需支付%.2f元" %(pricec,weightc,moneyc))
#格式化输出4，%,%.2意思是两位百分数
scale = 0.25
print("数据比列是%.2f%%" %(scale * 100))
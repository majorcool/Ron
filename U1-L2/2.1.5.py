grades = int(input("请输入您的成绩，满分100："))
if 60 >= grades >= 0:
    print("这都不及格，很刑啊！")
elif 90 >= grades > 60:
    print("及格了？但依旧拉跨！")
elif 100 > grades > 90:
    print("但是还不太行")
elif grades == 100:
    print("嗯？你竟然考上了100？不过，人外有人，天外有天doge")
elif grades > 100:
    print("什么？你的学习成绩竟然好到突破上限！快把我的豪华桌椅拿来！")

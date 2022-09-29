# 4.2.5 参考上节课练习 #3.3.2 的打印菱形，定义一个函数，能够根据不同的参数打印不同大小的菱形
def make_L(H):
    while True:
        finish = ""
        real_line = int(a)
        real_line = real_line //2 + 1
        for line in range(1,real_line+1):
            finish += (" "*(real_line-line))+("*"*(2*line-1))+"\n"
        for line in range(real_line-1,0,-1):
            finish += " "*(real_line-line)+"*"*(2*line-1)+"\n"
        return finish
a = int(input(":"))
print(make_L(a))
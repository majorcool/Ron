# 3.3.2 用户输入高度（行数），按照下方格式打印 1 个菱形
"""
  *
 ***
*****
 ***
  *
"""
while True:
    real_line = int(input("请输入行数（一个正奇数）"))
    if real_line % 2 == 0:
        print("请输入正奇数")
        continue
    real_line = real_line //2 + 1
    for line in range(1,real_line+1):
        print(" "*(real_line-line),end="")
        print("*"*(2*line-1))
    for line in range(real_line-1,0,-1):
        print(' '*(real_line-line),end='')
        print('*'*(2*line-1))




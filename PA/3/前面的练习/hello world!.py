import pygame
import sys  # sys 是 python 的标准库，提供 Python 运行时环境变量的操控


pygame.init()
size = width, height = 800, 600  # 窗口大小
screen = pygame.display.set_mode(size)  # 初始化窗口
pygame.display.set_caption('game')  # 窗口类型，左上角显示

hello = pygame.font.SysFont("宋体", 50)  # 实例化一个文本对象---字体; 字号---可以理解为创建一个预设
hello_1 = hello.render("Hello World!", True, (255, 255, 255))
# 用上面的实例(hello)渲染文字---文本; 可以理解为消除锯齿？True消，False不消; 颜色(RGB颜色模式)
screen.blit(hello_1, (300, 250))  # 在窗口(screen,前面初始化了)中渲染文字---渲染出的文本(hello_1); 位置(坐标)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()

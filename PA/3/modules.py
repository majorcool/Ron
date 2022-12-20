# color, display, draw, event, font, image, key, locals, mixer, mouse, rect, surface, time, music, pygame
import pygame
import sys  # sys 是 python 的标准库，提供 Python 运行时环境变量的操控


pygame.init()
size = width, height = 800, 600  # 窗口大小
screen = pygame.display.set_mode(size)  # 初始化窗口
pygame.display.set_caption('game')  # 窗口类型，左上角显示

hello = pygame.font.SysFont("Times New Roman", 50)
hello_1 = hello.render("color", True, (251, 128, 222))
screen.blit(hello_1, (0, 0))

pygame.draw.rect(screen, (25, 228, 22), (255, 122, 400, 200), 2)
# 绘制矩形---屏幕; 颜色; 位置坐标+长与宽; 是否填充0填充，其他数字设置边框宽度

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()



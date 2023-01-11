import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):  # 图像, 位置(二值)
        pygame.sprite.Sprite.__init__(self)

        self.image_0 = image
        self.rect_0 = self.image_0.get_rect()
        self.rect_0.left, self.rect_0.bottom = position

        self.image_1 = image
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.left, self.rect_1.bottom = self.rect_0.right, self.rect_0.bottom
        # left获取图像左边的数值(表示位置); right右边; bottom底部(下端)

        self.speed = speed
        self.displacement = 0

    def update(self):
        self.rect_0.left += self.speed
        self.rect_1.left += self.speed
        if self.rect_0.right < 0:
            self.rect_0.left = self.rect_1.right
            self.rect_0, self.rect_1 = self.rect_1, self.rect_0

    def draw(self, screen):
        screen.blit(self.image_0, self.rect_0)
        screen.blit(self.image_1, self.rect_1)

    def add_displacement(self):
        self.displacement += 1


class Cloud(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position

        self.speed = speed

    def update(self):
        self.rect.left += self.speed
        if self.rect.right < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


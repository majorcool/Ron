import pygame


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, images, position):
        pygame.sprite.Sprite.__init__(self)

        self.score = 0
        self.high_score = 0
        with open('high_score.py', 'r') as i:
            self.high_score = int(i.read().split('\n')[0])

        self.time = 0
        self.counter = 0
        self.light = "off"
        self.images = images
        self.image_score = self.rect_score = pygame.Surface((100, 31)).get_rect()
        self.image_high_score = self.rect_high_score = pygame.Surface((160, 31)).get_rect()
        self.rect_score.right, self.rect_score.top = position
        self.rect_high_score.right, self.rect_high_score.top = self.rect_score.left - 20, self.rect_score.top

    # def light_on(self):
    #     self.light = "on"
    #
    # def light_off(self):
    #     self.light = "off"

    def update(self):
        # stich current score image
        self.image_score = pygame.Surface((100, 31))
        self.image_score.fill((235, 235, 235))
        # if self.light == "on":
        #     self.counter += 1
        #     if 0 <= self.counter <= 1000:
        #         self.image_score.set_alpha(0, 0)
        #     if 20 < self.counter <= 2000:
        #         self.image_score.set_alpha(255, 0)
        #         self.counter = 0
        #         self.time += 1
        #     if self.time >= 4:
        #         self.time = 0
        #         self.light_off()
        for i, _ in enumerate(str(self.score).zfill(5)):  # current score images
            self.image_score.blit(self.images[int(_)], (20 * i, 0))

        # stitch high score image
        self.image_high_score = pygame.Surface((160, 31))
        self.image_high_score.fill((235, 235, 235))
        self.image_high_score.set_alpha(215, 0)
        self.image_high_score.blit(self.images[-1], (0, 0))
        for i, _ in enumerate(str(self.high_score).zfill(5)):  # highest score images
            self.image_high_score.blit(self.images[int(_)], (60 + 20 * i, 0))

    def draw(self, screen):
        screen.blit(self.image_score, self.rect_score)
        screen.blit(self.image_high_score, self.rect_high_score)


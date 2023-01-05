import pygame


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, images, position=(0, 300)):
        pygame.sprite.Sprite.__init__(self)

        self.position = position
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)
        self.status = "run"
        self.status_jump = "up"
        self.up_sound = "open"

        self.wait = 0
        self.t = 0
        self.velocity = 13
        self.refresh_rate = 5
        self.refresh_counter = 0
        self.stop_line = self.rect.bottom - self.rect.top + 50

    def jump(self):
        self.status = "jump"

    def fall(self):
        self.status_jump = "fall"

    def up(self):
        self.status_jump = "up"

    def run(self):
        self.status = "run"
        self.status_jump = "up"

    def open_sound(self):
        self.up_sound = "open"

    def close_sound(self):
        self.up_sound = "close"

    def duck(self):
        pass

    def unduck(self):
        pass

    def die(self):
        pygame.mixer.Sound('resources/audios/die.mp3').play()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def refresh(self):  # load_image
        if self.status == "run" or self.status == "jump":
            if self.image == self.images[0]:
                self.image = self.images[1]
            else:
                self.image = self.images[0]
            self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.status == "run" or self.status == "jump":
            if self.refresh_counter == self.refresh_rate:
                self.refresh()
                self.refresh_counter = 0
            self.refresh_counter += 1

        # if self.status == "jump":
            # if pygame.key.get_pressed()[pygame.K_SPACE]:
            #     self.t += 1
            #     self.rect.bottom -= self.velocity * self.t
            #     if self.rect.bottom <= self.stop_line:
            #         self.rect.bottom = self.stop_line
            #         self.t = 0
            # self.refresh()
            # if self.rect.bottom == self.stop_line or not pygame.key.get_pressed()[pygame.K_SPACE]:
            #     self.t += 1
            #     self.rect.bottom += self.velocity * self.t
            #     if self.rect.bottom > 300:
            #         self.rect.bottom = 300
            #         self.t = 0
            #         self.status = "run"
            # self.refresh()

        if self.status == "jump" and self.status_jump == "up":
            if self.up_sound == "open":
                pygame.mixer.Sound('resources/audios/jump.mp3').play()
                self.close_sound()
            self.rect.bottom -= self.velocity
            if self.rect.bottom <= self.stop_line:
                self.rect.bottom = self.stop_line
                self.fall()

        if self.status == "jump" and self.status_jump == "fall":
            self.wait += 1
            if self.wait > 7:
                self.rect.bottom += self.velocity
            if self.rect.bottom > 300:
                self.rect.bottom = 300
                self.run()
                self.open_sound()
                self.wait = 0

        if self.status == "duck":
            pass



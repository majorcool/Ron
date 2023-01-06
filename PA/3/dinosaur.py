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
        self.status = "start"
        self.status_jump = "up"
        self.status_jump_key = "close"
        self.up_sound = "open"
        self.die_sound = "open"

        self.wait = 0
        self.t = 0
        self.velocity = 13  # 13
        self.refresh_rate = 5
        self.refresh_counter = 0
        self.stop_line = self.rect.bottom - self.rect.top + 20

    def start_run(self):
        self.status = "run"

    def start(self):
        self.status = "start"

    def jump(self):
        self.status = "jump"

    def fall(self):
        self.status_jump = "fall"

    def up(self):
        self.status_jump = "up"

    def open_jump_key(self):
        self.status_jump_key = "open"

    def close_jump_key(self):
        self.status_jump_key = "close"

    def run(self):
        self.status = "run"
        self.status_jump = "up"

    def open_sound(self):
        self.up_sound = "open"

    def close_sound(self):
        self.up_sound = "close"

    def close_die_sound(self):
        self.die_sound = "close"

    def open_die_sound(self):
        self.die_sound = "open"

    def duck(self):
        self.status = "duck"

    def unduck(self):
        pass

    def die(self):
        if self.die_sound == "open":
            pygame.mixer.Sound('resources/audios/die.mp3').play()
            self.close_die_sound()
        self.status = "die"

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def refresh(self):  # load_image
        if self.status == "start":
            self.image = self.images[7]

        if self.status == "run":
            if self.image == self.images[0]:
                self.image = self.images[1]
            else:
                self.image = self.images[0]
            self.mask = pygame.mask.from_surface(self.image)
        if self.status == "jump":
            self.image = self.images[2]
            self.mask = pygame.mask.from_surface(self.image)
        if self.status == "duck":
            if self.image == self.images[3]:
                self.image = self.images[4]
            else:
                self.image = self.images[3]
            self.mask = pygame.mask.from_surface(self.image)
        if self.status == "die":
            self.image = self.images[5]

    def update(self):
        if self.status == "start":
            self.refresh()

        if self.status == "run" or self.status == "duck":
            if self.refresh_counter == self.refresh_rate:
                self.refresh()
                self.refresh_counter = 0
            self.refresh_counter += 1

        if self.status == "jump" and self.status_jump == "up":
            if self.up_sound == "open":
                pygame.mixer.Sound('resources/audios/jump.mp3').play()
                self.close_sound()
            self.rect.bottom -= self.velocity
            if self.rect.bottom <= self.stop_line:
                self.rect.bottom = self.stop_line
                self.fall()
            if self.status_jump_key == "close":
                self.fall()
            self.refresh()

        if self.status == "jump" and self.status_jump == "fall" or self.status == "jump" and self.status_jump == "fall" and self.status_jump_key == "close":
            self.wait += 1
            if self.wait > 7:  # 7
                self.rect.bottom += self.velocity
            if self.rect.bottom > 300:
                self.rect.bottom = 300
                self.run()
                self.open_sound()
                self.wait = 0
                self.up()
            self.refresh()

        if self.status == "die":
            self.refresh()



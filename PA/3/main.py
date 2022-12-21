import sys
import pygame
import random
from scene import Ground, Cloud

FPS = 60
TITLE = "Chrome Dino"
BACKGROUND_COLOR = (235, 235, 235)
SCREENSIZE = (700, 300)
IMAGE_PATHS = {
    "ground": "resources/images/ground.png",
    "cloud": "resources/images/cloud.png",
}
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)

image_ground = pygame.image.load(IMAGE_PATHS["ground"])
ground = Ground(image_ground, (0, SCREENSIZE[1]))

image_cloud = pygame.image.load(IMAGE_PATHS['cloud'])
cloud_sprites_group = pygame.sprite.Group()

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    # if len(cloud_sprites_group) < 5:
    if random.randint(0, 100) == 10:
        cloud_sprites_group.add(Cloud(image_cloud, (SCREENSIZE[0], random.randrange(30, 75))))

    ground.update()
    cloud_sprites_group.update()

    ground.draw(screen)
    cloud_sprites_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

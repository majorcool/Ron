import sys
import pygame
import random
from scene import Ground, Cloud
from obstacle import Cactus, Pterodactyl
from dinosaur import Dinosaur

FPS = 60
TITLE = "Chrome Dino"
BACKGROUND_COLOR = (235, 235, 235)
SCREENSIZE = (700, 300)
IMAGE_PATHS = {
    "ground": "resources/images/ground/ground.png",
    "cloud": "resources/images/cloud/cloud.png",
    "cactus1": "resources/images/cactus/cactus-1.png",
    "cactus2": "resources/images/cactus/cactus-2.png",
    "cactus3": "resources/images/cactus/cactus-3.png",
    "cactus4": "resources/images/cactus/cactus-4.png",
    "cactus5": "resources/images/cactus/cactus-5.png",
    "cactus6": "resources/images/cactus/cactus-6.png",
    "dinosaur1": "resources/images/dinosaur/dinosaur-1.png",
    "dinosaur2": "resources/images/dinosaur/dinosaur-2.png",
    "pterodactyl1": "resources/images/pterodactyl/pterodactyl-1.png",
    "pterodactyl2": "resources/images/pterodactyl/pterodactyl-2.png",
    "dinosaur-run-1": "resources/images/dinosaur/dinosaur-run-1.png",
    "dinosaur-run-2": "resources/images/dinosaur/dinosaur-run-2.png",
}
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)

image_ground = pygame.image.load(IMAGE_PATHS["ground"])
ground = Ground(image_ground, (0, SCREENSIZE[1]))

image_cloud = pygame.image.load(IMAGE_PATHS['cloud'])
cloud_sprites_group = pygame.sprite.Group()

image_cactus = []
for i in range(1, 7):
    __ = "cactus".replace("cactus", "cactus" + str(i))
    _ = pygame.image.load(IMAGE_PATHS[__])
    image_cactus.append(_)
cacti = pygame.sprite.Group()

image_pterodactyl = []
for i in range(1, 3):
    __ = "pterodactyl".replace("pterodactyl", "pterodactyl" + str(i))
    _ = pygame.image.load(IMAGE_PATHS[__])
    image_pterodactyl.append(_)
pterodactyls = pygame.sprite.Group()

clock = pygame.time.Clock()

image_dinosaur = []
for i in range(1, 3):
    __ = "dinosaur-run-".replace("dinosaur-run-", "dinosaur-run-" + str(i))
    _ = pygame.image.load(IMAGE_PATHS[__])
    image_dinosaur.append(_)
dinosaurs = pygame.sprite.Group()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    # if len(cloud_sprites_group) < 5:
    if random.randint(0, 100) == 10:
        cloud_sprites_group.add(Cloud(image_cloud, (SCREENSIZE[0], random.randrange(30, 75))))

    if random.randint(0, 100) == 10:
        cacti.add(Cactus(image_cactus, (SCREENSIZE[0], SCREENSIZE[1])))

    if random.randint(0, 100) == 10:
        pterodactyls.add(Pterodactyl(image_pterodactyl, (SCREENSIZE[0], random.randrange(20, 75))))

    if 1 == 1:
        dinosaurs.add(Dinosaur(image_dinosaur))

    ground.update()
    cloud_sprites_group.update()
    cacti.update()
    pterodactyls.update()
    dinosaurs.update()

    ground.draw(screen)
    cloud_sprites_group.draw(screen)
    cacti.draw(screen)
    pterodactyls.draw(screen)
    dinosaurs.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

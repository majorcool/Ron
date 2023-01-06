while True:
    import sys
    import pygame
    import random
    from scene import Ground, Cloud
    from obstacle import Cactus, Pterodactyl
    from dinosaur import Dinosaur
    from scoreboard import Scoreboard
    from ending import Ending

    out = ""
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
        "pterodactyl1": "resources/images/pterodactyl/pterodactyl-1.png",
        "pterodactyl2": "resources/images/pterodactyl/pterodactyl-2.png",
        "dinosaur1": "resources/images/dinosaur/dinosaur-run-1.png",
        "dinosaur2": "resources/images/dinosaur/dinosaur-run-2.png",
        "dinosaur3": "resources/images/dinosaur/dinosaur-jump.png",
        "dinosaur4": "resources/images/dinosaur/dinosaur-duck-1.png",
        "dinosaur5": "resources/images/dinosaur/dinosaur-duck-2.png",
        "dinosaur6": "resources/images/dinosaur/dinosaur-die-1.png",
        "dinosaur7": "resources/images/dinosaur/dinosaur-die-2.png",
        "dinosaur8": "resources/images/dinosaur/dinosaur-start.png",
        "scoreboard0": "resources/images/scoreboard/scoreboard-0.png",
        "scoreboard1": "resources/images/scoreboard/scoreboard-1.png",
        "scoreboard2": "resources/images/scoreboard/scoreboard-2.png",
        "scoreboard3": "resources/images/scoreboard/scoreboard-3.png",
        "scoreboard4": "resources/images/scoreboard/scoreboard-4.png",
        "scoreboard5": "resources/images/scoreboard/scoreboard-5.png",
        "scoreboard6": "resources/images/scoreboard/scoreboard-6.png",
        "scoreboard7": "resources/images/scoreboard/scoreboard-7.png",
        "scoreboard8": "resources/images/scoreboard/scoreboard-8.png",
        "scoreboard9": "resources/images/scoreboard/scoreboard-9.png",
        "scoreboard10": "resources/images/scoreboard/scoreboard-10.png",
        "ending0": "resources/images/ending/game-over.png",
        "ending1": "resources/images/ending/restart-1.png",
        "ending2": "resources/images/ending/restart-2.png",
        "ending3": "resources/images/ending/restart-3.png",
        "ending4": "resources/images/ending/restart-4.png",
        "ending5": "resources/images/ending/restart-5.png",
        "ending6": "resources/images/ending/restart-6.png",
        "ending7": "resources/images/ending/restart-7.png",
        "ending8": "resources/images/ending/restart-8.png",
    }
    pygame.init()
    screen = pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption(TITLE)

    speed = -10
    image_ground = pygame.image.load(IMAGE_PATHS["ground"])
    ground = Ground(image_ground, (0, SCREENSIZE[1]), speed)

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
    for i in range(1, 9):
        __ = "dinosaur".replace("dinosaur", "dinosaur" + str(i))
        _ = pygame.image.load(IMAGE_PATHS[__])
        image_dinosaur.append(_)
    dinosaurs = Dinosaur(image_dinosaur)

    image_scoreboard = []
    for i in range(0, 11):
        __ = "scoreboard".replace("scoreboard", "scoreboard" + str(i))
        _ = pygame.image.load(IMAGE_PATHS[__])
        image_scoreboard.append(_)
    scoreboards = Scoreboard(image_scoreboard, (680, 10))

    image_ending = []
    for i in range(0, 9):
        __ = "ending".replace("ending", "ending" + str(i))
        _ = pygame.image.load(IMAGE_PATHS[__])
        image_ending.append(_)
    endings = Ending(image_ending)

    while True:

        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pressed = pygame.key.get_pressed()

            if dinosaurs.status == "start":
                if pressed[pygame.K_SPACE] or pressed[pygame.K_UP]:
                    dinosaurs.start_run()

            if dinosaurs.status != "die":
                if dinosaurs.status != "duck":
                    if pressed[pygame.K_SPACE] or pressed[pygame.K_UP]:
                        dinosaurs.jump()
                        dinosaurs.open_jump_key()
                    else:
                        dinosaurs.close_jump_key()
                if dinosaurs.status == "run" or dinosaurs.status == "duck":
                    if pressed[pygame.K_DOWN]:
                        dinosaurs.duck()
                    if not pressed[pygame.K_DOWN]:
                        dinosaurs.run()

            if dinosaurs.status == "die":
                if pressed[pygame.K_SPACE] or pressed[pygame.MOUSEBUTTONDOWN] or pressed[pygame.K_UP]:
                    dinosaurs.start()
                    out = "break"
                    break

        if out == "break":
            break

        if dinosaurs.status != "die":
            dinosaurs.open_die_sound()

        for _ in pterodactyls:
            if pygame.sprite.collide_mask(dinosaurs, _):
                dinosaurs.die()  # self.status = 'die'
                dinosaurs.update()  # change image when dinosaur dies
                break

        for _ in cacti:
            if pygame.sprite.collide_mask(dinosaurs, _):
                dinosaurs.die()  # self.status = 'die'
                dinosaurs.update()  # change image when dinosaur dies
                break

        if dinosaurs.status == "die":
            scoreboards.high_score = max(scoreboards.score, scoreboards.high_score)
            with open('high_score.py', 'r+') as i:
                i.write(str(scoreboards.high_score))

        if dinosaurs.status != "start":
            if random.randint(0, 100) == 10:
                cloud_sprites_group.add(Cloud(image_cloud, (SCREENSIZE[0], random.randrange(30, 75)), speed))

            if random.randint(0, 100) == 10 and scoreboards.score >= 30:
                cacti.add(Cactus(image_cactus, (SCREENSIZE[0], SCREENSIZE[1]), speed))

            if random.randint(0, 100) == 10 and scoreboards.score >= 130:
                pterodactyls.add(Pterodactyl(image_pterodactyl, (SCREENSIZE[0], random.randrange(20, 75)), speed))

            ground.add_displacement()

        scoreboards.score = ground.displacement // 7  # algorithm of score
        if dinosaurs.status != "die":
            if scoreboards.score and not scoreboards.score % 100:
                pygame.mixer.Sound('resources/audios/score.mp3').play()  # sound
                speed -= 0.1
                # scoreboards.light_on()
                print("fefef")

        if dinosaurs.status != "die":
            ground.update()
            cloud_sprites_group.update()
            cacti.update()
            pterodactyls.update()
            dinosaurs.update()
            scoreboards.update()
        if dinosaurs.status == "die":
            endings.update()

        if dinosaurs.status != "start":
            ground.draw(screen)
            cloud_sprites_group.draw(screen)
            cacti.draw(screen)
            pterodactyls.draw(screen)
            scoreboards.draw(screen)
        dinosaurs.draw(screen)

        if dinosaurs.status == "die":
            endings.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

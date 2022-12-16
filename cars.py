import pygame, os, random, time

outro = False
STOP = False
while not STOP:

    WIDTH = 1000
    HEIGHT = 800
    FPS = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 200, 0)
    BLUE = (0, 130, 255)
    CK = (0, 255, 0)
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("plat1.1")
    clock = pygame.time.Clock()
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'img')
    ou_r = 0
    ou = 0
    screen.fill(BLUE)

    player_img = pygame.image.load(os.path.join(img_folder, 'pl-1.png')).convert()
    road_img = pygame.image.load(os.path.join(img_folder, 'rd-1.png')).convert()
    oil_img = pygame.image.load(os.path.join(img_folder, 'oi-1.png')).convert()
    bot_img = pygame.image.load(os.path.join(img_folder, 'bt-1.png')).convert()
    key_img = pygame.image.load(os.path.join(img_folder, 'ky-1.png')).convert()
    key_img.set_colorkey(CK)

    sm_11_img = pygame.image.load(os.path.join(img_folder, 'sm-11.png')).convert()
    sm_12_img = pygame.image.load(os.path.join(img_folder, 'sm-12.png')).convert()
    sm_13_img = pygame.image.load(os.path.join(img_folder, 'sm-13.png')).convert()
    sm_14_img = pygame.image.load(os.path.join(img_folder, 'sm-14.png')).convert()
    sm_11_img.set_colorkey(CK)
    sm_12_img.set_colorkey(CK)
    sm_13_img.set_colorkey(CK)
    sm_14_img.set_colorkey(CK)
    """
    sm_21_img = pygame.image.load(os.path.join(img_folder, 'sm-21.png')).convert()
    sm_22_img = pygame.image.load(os.path.join(img_folder, 'sm-22.png')).convert()
    sm_23_img = pygame.image.load(os.path.join(img_folder, 'sm-23.png')).convert()
    sm_24_img = pygame.image.load(os.path.join(img_folder, 'sm-24.png')).convert()
    sm_21_img.set_colorkey(CK)
    sm_22_img.set_colorkey(CK)
    sm_23_img.set_colorkey(CK)
    sm_24_img.set_colorkey(CK)

    sm_31_img = pygame.image.load(os.path.join(img_folder, 'sm-31.png')).convert()
    sm_32_img = pygame.image.load(os.path.join(img_folder, 'sm-32.png')).convert()
    sm_33_img = pygame.image.load(os.path.join(img_folder, 'sm-33.png')).convert()
    sm_34_img = pygame.image.load(os.path.join(img_folder, 'sm-34.png')).convert()
    sm_31_img.set_colorkey(CK)
    sm_32_img.set_colorkey(CK)
    sm_33_img.set_colorkey(CK)
    sm_34_img.set_colorkey(CK)
    """
    ps_1_img = pygame.image.load(os.path.join(img_folder, 'ps-1.png')).convert()
    ps_11_img = pygame.image.load(os.path.join(img_folder, 'ps-11.png')).convert()
    ps_2_img = pygame.image.load(os.path.join(img_folder, 'ps-2.png')).convert()
    ps_21_img = pygame.image.load(os.path.join(img_folder, 'ps-21.png')).convert()
    ps_3_img = pygame.image.load(os.path.join(img_folder, 'ps-3.png')).convert()
    ps_31_img = pygame.image.load(os.path.join(img_folder, 'ps-31.png')).convert()
    ps_4_img = pygame.image.load(os.path.join(img_folder, 'ps-4.png')).convert()
    ps_41_img = pygame.image.load(os.path.join(img_folder, 'ps-41.png')).convert()
    ps_1_img.set_colorkey(CK)
    ps_11_img.set_colorkey(CK)
    ps_2_img.set_colorkey(CK)
    ps_21_img.set_colorkey(CK)
    ps_3_img.set_colorkey(CK)
    ps_31_img.set_colorkey(CK)
    ps_4_img.set_colorkey(CK)
    ps_41_img.set_colorkey(CK)

    key_rect = key_img.get_rect()
    sm_rect = sm_11_img.get_rect()
    all_sprites = pygame.sprite.Group()
    running = True
    Flip = False
    flip = 0
    hp = 100
    up = 0
    down = 0
    left = 0
    right = 0
    UP = 0
    DOWN = 0
    LEFT = 0
    RIGHT = 0
    points = 0
    d = 0
    DMG = 0
    stop = 0
    push = 0
    resW = 180
    resS = 300
    e = 0
    scal = 0
    pause = False
    p = 10
    ran = 0
    shake = 0
    menu = True
    shk_off = -1
    FLIP = 0
    smc = 1
    smd = 0
    ty = [0, 0, 0, 0, 0, 0, 0, 0]

    class Road(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = road_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def update(self):
            if not pause:
                self.rect.y += 15
            if self.rect.y >= 0:
                self.rect.y = -1000

    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = player_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def update(self):
            global keys, Flip, player_img, flip, hp, up, down, left, right, i, UP, DOWN, RIGHT, LEFT, push, resW, resS, scal, oil_img, shake, FLIP
            keys = pygame.key.get_pressed()
            if not pause and not menu:
                flip = 0
                if resW < 180:
                    resW += 1
                if resS < 300:
                    resS += 1
                if keys[pygame.K_w] and resW >= 180:
                    push = 4
                    resW = 0
                    Wrect.width = 10
                    Wrect.height = 10
                if keys[pygame.K_s] and resS >= 300:
                    oil.rect.y = self.rect.y - 120
                    oil.rect.x = self.rect.x - 120
                    resS = 0
                    oil_img = pygame.transform.scale(oil_img, (50, 50))
                    oil.__init__(oil.rect.centerx, oil.rect.centery)
                    scal = 50
                if oil.rect.x <= 200:
                    oil.rect.x = 200
                if oil.rect.right >= 800:
                    oil.rect.right = 800

                if self.rect.x <= 200:
                    self.rect.x += 1
                if self.rect.right >= 800:
                    self.rect.x -= 1
                if not keys[pygame.K_SPACE]:
                    if not (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
                        if keys[pygame.K_LEFT] and self.rect.x >= 250:
                            if not Flip:
                                FLIP = 1
                                flip = 1
                            self.rect.x -= 5
                            left = 5
                            for i in bots:
                                if i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 20 and i.rect.right >= self.rect.x + 15 + ((i.rect.y - self.rect.y) / 4) and i.rect.x <= self.rect.right - 50:
                                    i.rect.x -= 2
                                    self.rect.x += 3
                                    left = 0
                                    for _ in bots:
                                        if _ != i:
                                            if _.rect.x >= 250:
                                                if _.rect.y <= i.rect.bottom and _.rect.bottom >= i.rect.y + 20 and _.rect.right >= i.rect.x + 20 and _.rect.x <= i.rect.right - 20:
                                                    _.rect.x -= 5
                                            else:
                                                self.rect.x += 5
                                                i.rect.x += 5
                                    if i.rect.x <= 250:
                                        self.rect.x += 5
                                        i.rect.x += 5
                        elif keys[pygame.K_RIGHT] and self.rect.x <= 660:
                            if not Flip:
                                FLIP = -1
                                flip = -1
                            self.rect.x += 5
                            right = 5
                            for i in bots:
                                if i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 20 and i.rect.right >= self.rect.x + 50 and i.rect.x <= self.rect.right - 15 - ((i.rect.y - self.rect.y) / 4):
                                    i.rect.x += 2
                                    self.rect.x -= 3
                                    right = 0
                                    for _ in bots:
                                        if _ != i:
                                            if _.rect.right <= 750:
                                                if _.rect.y <= i.rect.bottom and _.rect.bottom >= i.rect.y + 20 and _.rect.right >= i.rect.x + 20 and _.rect.x <= i.rect.right - 20:
                                                    _.rect.x += 5
                                            else:
                                                self.rect.x -= 5
                                                i.rect.x -= 5
                                    if i.rect.right >= 750:
                                        self.rect.x -= 5
                                        i.rect.x -= 5
                        else:
                            flip = 0
                            FLIP = 0
                            Flip = False
                    if keys[pygame.K_UP] and self.rect.y >= 50:
                        self.rect.y -= 5
                        up = 5
                        for i in bots:
                            if i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 20 and i.rect.x <= self.rect.right - 20:
                                i.rect.y -= 2
                                self.rect.y += 3
                    if keys[pygame.K_DOWN] and self.rect.bottom <= 700:
                        self.rect.y += 5
                        down = 5
                        for i in bots:
                            if i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 20 and i.rect.x <= self.rect.right - 20:
                                i.rect.y += 2
                                self.rect.y -= 3
                    for i in bots:
                        if up > 0 and not keys[pygame.K_UP] and self.rect.y >= 50 and not (i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 10 and i.rect.x <= self.rect.right - 10):
                            UP += 1
                    if UP > 0:
                        self.rect.y -= up
                        up -= 0.3
                        UP = 0
                    for i in bots:
                        if down > 0 and not keys[pygame.K_DOWN] and self.rect.bottom <= 700 and not (i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 10 and i.rect.x <= self.rect.right - 10):
                            DOWN += 1
                    if DOWN > 0:
                        self.rect.y += down
                        down -= 0.3
                        DOWN = 0
                    for i in bots:
                        if left > 0 and not keys[pygame.K_LEFT] and self.rect.x >= 250 and not (i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 10 and i.rect.x <= self.rect.right - 10):
                            LEFT += 1
                    if LEFT > 0:
                        self.rect.x -= left
                        left -= 0.5
                        LEFT = 0
                    for i in bots:
                        if right > 0 and not keys[pygame.K_RIGHT] and self.rect.x <= 660 and not (i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 10 and i.rect.x <= self.rect.right - 10):
                            RIGHT += 1
                    if RIGHT > 0:
                        self.rect.x += right
                        right -= 0.5
                        RIGHT = 0
                else:
                    up = 0; down = 0; left = 0; right = 0

                if flip == 1:
                    player_img = pygame.transform.rotate(player_img, 15)
                    Flip = True
                    self.__init__(self.rect.centerx, self.rect.centery)
                elif flip == -1:
                    player_img = pygame.transform.rotate(player_img, -15)
                    Flip = True
                    self.__init__(self.rect.centerx, self.rect.centery)
                if (not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]) or (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
                    Flip = False
                    player_img = pygame.image.load(os.path.join(img_folder, 'pl-1.png')).convert()
                    self.__init__(self.rect.centerx, self.rect.centery)

    class Bot(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = bot_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def update(self):
            global i, hp, r, DMG, _, stop, push, shake
            if not pause and not menu:
                push /= 1.03
                if push <= 1.5:
                    push = 0
                for i in bots:
                    if i.rect.y >= 800:
                        i.rect.y = -100
                        r = random.randint(0, 3)
                        if r == 0:
                            i.rect.centerx = 310
                        elif r == 1:
                            i.rect.centerx = 440
                        elif r == 2:
                            i.rect.centerx = 580
                        elif r == 3:
                            i.rect.centerx = 700
                    if i.rect.y <= player.rect.bottom and i.rect.bottom >= player.rect.y and i.rect.right >= player.rect.x + 10 and i.rect.x <= player.rect.right - 10:
                        DMG += 1
                    if i.rect.y <= player.rect.y + 10 and i.rect.bottom >= player.rect.y + 10 and i.rect.right >= player.rect.x + 20 and i.rect.x <= player.rect.right - 20:
                        i.rect.y -= 4
                    for _ in bots:
                        if _ != i:
                            if i.rect.y <= _.rect.bottom - 50 and i.rect.bottom >= _.rect.y + 10 and i.rect.right >= _.rect.x + 20 and i.rect.x <= _.rect.right - 20 and i.rect.bottom >= 0:
                                i.rect.y -= 4
                            if i.rect.y <= _.rect.bottom - 50 and i.rect.bottom >= _.rect.y + 10 and i.rect.right >= _.rect.x + 20 and i.rect.x <= _.rect.right - 20 and i.rect.bottom <= 0:
                                i.rect.x += 10
                                i.rect.y -= 100
                    if stop > 9:
                        i.rect.y -= 7
                        stop = 0
                    for _ in bots:
                        if _ != i:
                            if not (i.rect.y <= _.rect.bottom and i.rect.bottom >= _.rect.y and i.rect.right >= _.rect.x and i.rect.x <= _.rect.right):
                                if i.rect.right <= player.rect.x and i.rect.x >= 250 and push > 0:
                                    i.rect.x -= push
                                elif i.rect.x >= player.rect.right and i.rect.right <= 660 and push > 0:
                                    i.rect.x += push
                                if i.rect.bottom <= player.rect.y and push > 0:
                                    i.rect.y -= push
                                elif i.rect.y >= player.rect.bottom and push > 0:
                                    i.rect.y += push
                self.rect.y += 4
                if DMG > 0:
                    shake += 1 / len(bots)
                    hp -= 0.01
                    DMG = 0

    class Oil(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = oil_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def update(self):
            global i, e, oil_img, scal
            if not pause and not menu:
                self.rect.y += 15
                for i in bots:
                    if i.rect.x <= self.rect.right and i.rect.right >= self.rect.x and i.rect.y <= self.rect.bottom - 170 and i.rect.bottom >= self.rect.y:
                        i.rect.y += 11
                
                if scal < 300:
                    scal += 10

                oil_img = pygame.image.load(os.path.join(img_folder, 'oi-1.png')).convert()
                oil_img = pygame.transform.scale(oil_img, (scal, scal))
                self.__init__(self.rect.centerx, self.rect.centery)


    font_type = pygame.font.Font('Teletactile.ttf', 20)
    text = font_type.render((str("Points: ") + str(points)), True, (0, 0, 0))

    road = Road(500, 0)
    oil = Oil(500, 1000)
    player = Player(500, 700)
    bot1 = Bot(300, -400)
    bot2 = Bot(440, -250)
    bot3 = Bot(580, -300)
    bot4 = Bot(700, -500)

    all_sprites.add(road)
    all_sprites.add(oil)
    all_sprites.add(player)
    all_sprites.add(bot1, bot2, bot3, bot4)

    bots = [bot1, bot2, bot3, bot4]

    sm1 = [sm_11_img, sm_12_img, sm_13_img, sm_14_img]
    #sm2 = [sm_21_img, sm_22_img, sm_23_img, sm_24_img]
    #sm3 = [sm_31_img, sm_32_img, sm_33_img, sm_34_img]

    textW = font_type.render((str("W")), True, (0, 0, 0))
    textS = font_type.render((str("S")), True, (0, 0, 0))
    Wrect = key_img.get_rect()
    Wrect.width = 3000
    Wrect.height = 3000


    while running:
        clock.tick(FPS)
        
        w = 0
        shake = int(shake)
        if shk_off == 1:
            shake = 0
        ran = random.randint(-shake, shake)
        shake = 0
        keys = pygame.key.get_pressed()
        p -= 1
        if keys[pygame.K_ESCAPE] and not menu:
            if p <= 0:
                if not pause:
                    pause = True
                    p = 15
                else:
                    pause = False
                    p = 15
    #----------------------------------------------------------------#
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                STOP = True
            elif event.type == pygame.MOUSEMOTION:
                ty = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                w = event.button
    #----------------------------------------------------------------#
        if hp >= 0:
            all_sprites.remove()
            all_sprites.update()
    #----------------------------------------------------------------#
        Wrect.centerx = player.rect.centerx; Wrect.centery = player.rect.centery
        if not pause:
            Wrect.width += 70
            Wrect.height += 70
            shake += 3000 / Wrect.width
            if d >= 30 and hp > 0:
                if not pause and not menu:
                    points += 1
                d = 0
                text = font_type.render((str("Points: ") + str(points)), True, (0, 0, 0))
            else:
                d += 1
        for i in all_sprites:
            i.rect.x += ran
        all_sprites.draw(screen)
        for i in all_sprites:
            i.rect.x -= ran
        screen.blit(text, (770, 20))
        screen.blit(key_img, (10, 10), key_rect)
        pygame.draw.rect(screen, "black", (55, 15, 110, 30))
        pygame.draw.rect(screen, "orange", (60, 20, hp, 20))
        pygame.draw.circle(screen, "black", (50, 100), 34)
        pygame.draw.circle(screen, "white", (50, 100), resW / 6)
        screen.blit(textW, (42, 90))
        pygame.draw.circle(screen, "black", (50, 200), 34)
        pygame.draw.circle(screen, "white", (50, 200), resS / 10)
        screen.blit(textS, (42, 190))
        if Wrect.width <= 2000:
            pygame.draw.arc(screen, "white", Wrect, 0, 30, 100)
    #--------------------пауза--------------------------------------#
        smd += 1
        if smd >= 15:
            smd = 0
            smc += 1
            if smc >= 4:
                smc = 0
            sm_img = sm1[smc]
        if hp <= 50:
            if FLIP == -1:
                screen.blit(sm_img, (player.rect.x + 30, player.rect.y), sm_rect)
            else:
                screen.blit(sm_img, (player.rect.x, player.rect.y), sm_rect)
    #----------------------------------------------------------------#
        if pause:
            if ty[0] >= 355 and ty[1] >= 300 and ty[0] <= 355 + 300 and ty[1] <= 370:
                screen.blit(ps_1_img, (355, 300))
                if w == 1:
                    pause = False
            else:
                screen.blit(ps_11_img, (355, 300))
        if pause or menu:
            if ty[0] >= 355 and ty[1] >= 400 and ty[0] <= 355 + 300 and ty[1] <= 470:
                screen.blit(ps_2_img, (355, 400))
                if w == 1:
                    shk_off *= -1
            else:
                screen.blit(ps_21_img, (355, 400))
        if pause:
            if ty[0] >= 355 and ty[1] >= 500 and ty[0] <= 355 + 300 and ty[1] <= 570:
                screen.blit(ps_3_img, (355, 500))
                if w == 1:
                    running = False
                    ou_r = 0
                    while ou_r <= 1010:
                        pygame.draw.rect(screen, BLACK, (0, 0, ou_r, 1000))
                        ou_r += 5
                        pygame.display.flip()
            else:
                screen.blit(ps_31_img, (355, 500))
        if menu:
            if ty[0] >= 355 and ty[1] >= 500 and ty[0] <= 355 + 300 and ty[1] <= 570:
                screen.blit(ps_3_img, (355, 500))
                if w == 1:
                    running = False
                    STOP = True
            else:
                screen.blit(ps_31_img, (355, 500))
        if menu:
            if keys[pygame.K_SPACE]:
                menu = False
            if ty[0] >= 355 and ty[1] >= 300 and ty[0] <= 355 + 300 and ty[1] <= 370:
                screen.blit(ps_4_img, (355, 300))
                if w == 1:
                    menu = False
            else:
                screen.blit(ps_41_img, (355, 300))
    #----------------------------------------------------------------#
        outro = True
        if outro and ou_r <= 1010:
            pygame.draw.rect(screen, BLACK, (ou_r, 0, 1000, 1000))
            ou_r += 25
    #----------------------------------------------------------------#
        pygame.display.flip()

pygame.quit()

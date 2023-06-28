import pygame, os, random

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
    cop_nr_img = pygame.image.load(os.path.join(img_folder, 'pc-1.png')).convert()
    cop_cr_img = pygame.image.load(os.path.join(img_folder, 'pc-2.png')).convert()
    cop_img = cop_nr_img
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
    dodge = False
    direction = 0
    band_list = []
    free_band = []
    cop_band = 0
    dodge_ = 0
    CoPdOwN = False
    CoPdOwNN = 4
    cop_stun = 0
    cop_flip = False
    cop_to_plus = False
    cop_to_minus = False
    cop_stop = False

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
            global keys, Flip, player_img, flip, hp, up, down, left, right, i, UP, DOWN, RIGHT, LEFT, push, resW, resS, scal, oil_img, shake, FLIP, cop_stop
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

                if self.rect.y >= 800:
                    self.rect.y = 300
                    self.rect.centerx = 508
                    hp -= 5
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
                            if cop.rect.y <= self.rect.bottom and cop.rect.bottom >= self.rect.y + 20 and cop.rect.right >= self.rect.x + 15 + ((cop.rect.y - self.rect.y) / 4) and cop.rect.x <= self.rect.right - 50:
                                self.rect.x += 3
                                cop.rect.x -= 2
                                left = 0
                                cop_stop = True
                                shake += 2
                                for _ in bots:
                                    if _.rect.right <= 750:
                                        if _.rect.y <= cop.rect.bottom and _.rect.bottom >= cop.rect.y + 20 and _.rect.right >= cop.rect.x + 20 and _.rect.x <= cop.rect.right - 20:
                                            _.rect.x -= 5
                                    else:
                                        self.rect.x += 5
                                        cop.rect.x += 5
                            else: cop_stop = False
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
                            if cop.rect.y <= self.rect.bottom and cop.rect.bottom >= self.rect.y + 20 and cop.rect.right >= self.rect.x + 50 and cop.rect.x <= self.rect.right - 15 - ((cop.rect.y - self.rect.y) / 4):
                                self.rect.x -= 3
                                cop.rect.x += 2
                                right = 0
                                cop_stop = True
                                shake += 2
                                for _ in bots:
                                    if _.rect.right <= 750:
                                        if _.rect.y <= cop.rect.bottom and _.rect.bottom >= cop.rect.y + 20 and _.rect.right >= cop.rect.x + 20 and _.rect.x <= cop.rect.right - 20:
                                            _.rect.x += 5
                                    else:
                                        self.rect.x -= 5
                                        cop.rect.x -= 5
                            else: cop_stop = False
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
                        if cop.rect.y <= self.rect.bottom and cop.rect.bottom >= self.rect.y + 10 and cop.rect.right >= self.rect.x + 20 and cop.rect.x <= self.rect.right - 20:
                            shake += 2
                            if not CoPdOwN:
                                up = 0
                                cop.rect.y -= 2
                                self.rect.y += 3
                            else:
                                up = 0
                                self.rect.y += 5
                        for i in bots:
                            if i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 20 and i.rect.x <= self.rect.right - 20:
                                i.rect.y -= 2
                                self.rect.y += 3
                    if keys[pygame.K_DOWN] and self.rect.bottom <= 700:
                        self.rect.y += 5
                        down = 5
                        if cop.rect.y <= self.rect.bottom and cop.rect.bottom >= self.rect.y + 10 and cop.rect.right >= self.rect.x + 20 and cop.rect.x <= self.rect.right - 20:
                            shake += 2
                            if not CoPdOwN:
                                down = 0
                                cop.rect.y += 2
                                self.rect.y -= 3
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
            global i, hp, r, DMG, _, stop, push, shake, band_list
            if not pause and not menu:
                band_list = []
                push /= 1.03
                if push <= 1.5:
                    push = 0
                for i in bots:
                    if i.rect.x >= 639:
                        band_list.append(3)
                    elif i.rect.x >= 508:
                        band_list.append(2)
                    elif i.rect.x >= 378:
                        band_list.append(1)
                    elif i.rect.right >= 0:
                        band_list.append(0)
                    
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

    class Cop(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = cop_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
        
        def update(self):
            global dodge, dodge_, cop_band, free_band, CoPdOwN, CoPdOwNN, cop_stun, cop_img, cop_flip, cop_to_plus, cop_to_minus, shake, hp
            if not pause and not menu:
                dodge = False
                cop_to_plus = False
                cop_to_minus = False

                if self.rect.x >= 639:
                    cop_band = 3
                elif self.rect.x >= 508:
                    cop_band = 2
                elif self.rect.x >= 378:
                    cop_band = 1
                elif self.rect.right >= 0:
                    cop_band = 0

                free_band = [0, 1, 2, 3]
                for i in band_list:
                    for _ in free_band:
                        if _ == i:
                            free_band.remove(i)
                CoPdOwNN = 4
                for i in bots:
                    if i.rect.y <= cop.rect.bottom and i.rect.bottom >= cop.rect.y and i.rect.right >= cop.rect.x + 10 and i.rect.x <= cop.rect.right - 10:
                        CoPdOwN = True
                    else: CoPdOwNN -= 1
                if CoPdOwNN == 0 and self.rect.y >= 900: CoPdOwN = False
                
                if oil.rect.y <= cop.rect.bottom and oil.rect.bottom >= cop.rect.y and oil.rect.right >= cop.rect.x + 10 and oil.rect.x <= cop.rect.right - 10:
                    self.rect.y += 7
                    CoPdOwN = True
                if cop.rect.right <= player.rect.x and cop.rect.x >= 250 and push > 0:
                    cop.rect.x -= push * 10
                    cop_stun = 120
                elif cop.rect.x >= player.rect.right and cop.rect.right <= 660 and push > 0:
                    cop.rect.x += push * 10
                    cop_stun = 120
                if cop.rect.bottom <= player.rect.y and push > 0:
                    cop.rect.y -= push * 10
                    cop_stun = 120
                elif cop.rect.y >= player.rect.bottom and push > 0:
                    cop.rect.y += push * 10
                    cop_stun = 120

                if CoPdOwN and not cop_flip:
                    cop_img = cop_cr_img
                    self.__init__(self.rect.centerx, self.rect.centery)
                    cop_flip = True
                    shake += 5
                elif not CoPdOwN:
                    cop_img = cop_nr_img
                    self.__init__(self.rect.centerx, self.rect.centery)
                    cop_flip = False

                cop_stun -= 1

                if CoPdOwN and self.rect.y >= 800:
                    self.rect.y = 3000

                if free_band != []:
                    for i in free_band:
                        if cop_band == i:
                            dodge_ = 0
                            break
                        elif cop_band - i < 0:
                            dodge_ = 1
                        elif cop_band - i > 0:
                            dodge_ = -1
                else: dodge_ = 0
            
                if cop_stun <= 0:
                    if not CoPdOwN and not (player.rect.y <= cop.rect.bottom and player.rect.bottom >= cop.rect.y and player.rect.right >= cop.rect.x + 10 and player.rect.x <= cop.rect.right - 10) and not cop_stop:
                        self.rect.x += 10 * dodge_
                    if not CoPdOwN:
                        if self.rect.y >= 400 and not (player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 35 and player.rect.right >= self.rect.x + 25 and player.rect.x <= self.rect.right - 25):
                            self.rect.y -= 5

                    if dodge_ == 0:
                        if cop_band == 0 and (self.rect.centerx <= 310 or self.rect.centerx >= 320):
                            if self.rect.centerx <= 310:
                                cop_to_plus = True
                            if self.rect.centerx >= 320:
                                cop_to_minus = True
                        if cop_band == 1 and (self.rect.centerx <= 440 or self.rect.centerx >= 450):
                            if self.rect.centerx <= 440:
                                cop_to_plus = True
                            if self.rect.centerx >= 450:
                                cop_to_minus = True
                        if cop_band == 2 and (self.rect.centerx <= 570 or self.rect.centerx >= 580):
                            if self.rect.centerx <= 570:
                                cop_to_plus = True
                            if self.rect.centerx >= 580:
                                cop_to_minus = True
                        if cop_band == 3 and (self.rect.centerx <= 690 or self.rect.centerx >= 700):
                            if self.rect.centerx <= 690:
                                cop_to_plus = True
                            if self.rect.centerx >= 700:
                                cop_to_minus = True
                    
                    if CoPdOwN:
                        self.rect.y += 4
                        if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y + 10 and player.rect.right >= self.rect.x + 25 and player.rect.x <= self.rect.right - 25:
                            player.rect.y += 4
                            hp -= 0.1

                    if not CoPdOwN and not cop_stop:
                        if cop_to_plus:
                            self.rect.x += 5
                            if player.rect.y <= cop.rect.bottom and player.rect.bottom >= cop.rect.y and player.rect.right >= cop.rect.x + 10 and player.rect.x <= cop.rect.right - 10:
                                self.rect.x -= 3
                                player.rect.x += 2
                                shake += 2
                            for i in bots:
                                if i.rect.y <= cop.rect.bottom and i.rect.bottom >= cop.rect.y and i.rect.right >= cop.rect.x + 10 and i.rect.x <= cop.rect.right - 10:
                                    self.rect.x -= 5
                                    shake += 1
                        elif cop_to_minus:
                            self.rect.x -= 5
                            if player.rect.y <= cop.rect.bottom and player.rect.bottom >= cop.rect.y and player.rect.right >= cop.rect.x + 10 and player.rect.x <= cop.rect.right - 10:
                                self.rect.x += 3
                                player.rect.x -= 2
                                shake += 2
                            for i in bots:
                                if i.rect.y <= cop.rect.bottom and i.rect.bottom >= cop.rect.y and i.rect.right >= cop.rect.x + 10 and i.rect.x <= cop.rect.right - 10:
                                    self.rect.x += 5
                                    shake += 1


    font_type = pygame.font.Font('Teletactile.ttf', 20)
    text = font_type.render((str("Points: ") + str(points)), True, (0, 0, 0))

    road = Road(500, 0)
    oil = Oil(500, 10000)
    player = Player(508, 700)
    cop = Cop(550, 1100)
    bot1 = Bot(300, -400)
    bot2 = Bot(440, -250)
    bot3 = Bot(580, -300)
    bot4 = Bot(700, -500)

    all_sprites.add(road)
    all_sprites.add(oil)
    all_sprites.add(player)
    all_sprites.add(cop)
    all_sprites.add(bot1, bot2, bot3, bot4)

    bots = [bot1, bot2, bot3, bot4]

    sm1 = [sm_11_img, sm_12_img, sm_13_img, sm_14_img]

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

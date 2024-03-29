import pygame, os, random, math
import functions
from PIL import Image, ImageFilter
import tkinter
#Переменные для анимации входа/выхода
outro = False
STOP = False
while not STOP:
    #Основные переменные
    WIDTH = 1000
    HEIGHT = 800
    FPS = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 200, 0)
    BLUE = (0, 130, 255)
    CK = (0, 255, 0)
    P_init = pygame.init()
    #pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("cars")
    clock = pygame.time.Clock()
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'img')
    ou_r = 0
    ou = 0
    screen.fill(BLUE)
    DataFile = open("data.txt", "r")
    data = DataFile.read()
    DataFile.close()

    #Переменные для работы с файлом
    skins = 5
    skin = 1

    data = data.split("\n")
    record = int(data[0])
    coins = int(data[1])
    sk = data[2]
    SK = []
    for i in sk:
        SK.append(i)
    prices = [0, 100, 100, 400, 200]

    #Загрузка изображений, подгон их под размер и выделение цветового ключа, создание rect`ов
    player_img = pygame.image.load(os.path.join(img_folder, ("pl-" + str(skin) + ".png"))).convert()
    road_img = pygame.image.load(os.path.join(img_folder, 'rd-1.png')).convert()
    oil_img = pygame.image.load(os.path.join(img_folder, 'oi-1.png')).convert()
    bot_img = pygame.image.load(os.path.join(img_folder, 'bt-1.png')).convert()
    cop_nr_img = pygame.image.load(os.path.join(img_folder, 'pc-1.png')).convert()
    cop_cr_img = pygame.image.load(os.path.join(img_folder, 'pc-2.png')).convert()
    cop_at_img = pygame.image.load(os.path.join(img_folder, 'pc-3.png')).convert()
    bul_img = pygame.image.load(os.path.join(img_folder, 'bl-1.png')).convert()
    dron_img = pygame.image.load(os.path.join(img_folder, 'dr-1.png')).convert()
    pit_img = pygame.image.load(os.path.join(img_folder, 'pt-1.png')).convert()
    spikes_img = pygame.image.load(os.path.join(img_folder, 'sp-1.png')).convert()
    coin_img = pygame.image.load(os.path.join(img_folder, 'cn-1.png')).convert()
    cop_img = cop_nr_img
    spark_img = pygame.image.load(os.path.join(img_folder, 'sr-1.png')).convert()
    blur_img = pygame.image.load('screen.png').convert()
    key_img = pygame.image.load(os.path.join(img_folder, 'ky-1.png')).convert()
    arrow_img = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'ar-1.png')).convert(), (80, 80))
    arrow_img.set_colorkey(CK)
    key_img.set_colorkey(CK)
    spark_img.set_colorkey(CK)
    dron_img.set_colorkey(CK)

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
    ps_5_img = pygame.image.load(os.path.join(img_folder, 'ps-5.png')).convert()
    ps_51_img = pygame.image.load(os.path.join(img_folder, 'ps-51.png')).convert()
    ps_6_img = pygame.transform.flip(ps_5_img, True, False)
    ps_61_img = pygame.transform.flip(ps_51_img, True, False)
    ps_7_img = pygame.image.load(os.path.join(img_folder, 'ps-6.png')).convert()
    ps_71_img = pygame.image.load(os.path.join(img_folder, 'ps-61.png')).convert()
    ps_8_img = pygame.image.load(os.path.join(img_folder, 'ps-7.png')).convert()
    ps_81_img = pygame.image.load(os.path.join(img_folder, 'ps-71.png')).convert()
    ps_1_img.set_colorkey(CK)
    ps_11_img.set_colorkey(CK)
    ps_2_img.set_colorkey(CK)
    ps_21_img.set_colorkey(CK)
    ps_3_img.set_colorkey(CK)
    ps_31_img.set_colorkey(CK)
    ps_4_img.set_colorkey(CK)
    ps_41_img.set_colorkey(CK)
    ps_5_img.set_colorkey(CK)
    ps_51_img.set_colorkey(CK)
    ps_6_img.set_colorkey(CK)
    ps_61_img.set_colorkey(CK)
    ps_7_img.set_colorkey(CK)
    ps_71_img.set_colorkey(CK)
    ps_8_img.set_colorkey(CK)
    ps_81_img.set_colorkey(CK)

    arrow_rect = arrow_img.get_rect()
    key_rect = key_img.get_rect()
    dron_rect = oil_img.get_rect()
    spark_rect = spark_img.get_rect()
    sm_rect = sm_11_img.get_rect()
    blur_rect = blur_img.get_rect()

    #Переменные, использующиеся в коде
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
    #Кд способностей
    resW = 1800
    resS = 3000
    resD = 600
    resA = 4800
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
    ty = [0, 0, 0, 0, 0, 0, 0, 0] #Массив для работы мышки, НЕ ТРОГАТЬ
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
    bot_spawn = True
    cop_attack = False
    at_c = 0
    ATTACK = "central"
    attack_list = ["central", "side", "spikes", "bull"]
    cenAt_c = 0
    cenAt_d = 0
    bul_x = 0
    bul_y = 0
    cenAt_x = 500
    cenAt_y = 400
    cop_hp = 0
    D = False
    A = 1
    move_speed = -15
    bot_count = 5 #Количество ботов (можно ставить сколько угодно, желательно до 20)
    bots = []
    dron_x, dron_y = 0, 0
    okr_b = 0
    sidAt_s = 0
    sidAt_c = 0
    pit_c = 0
    pit_pl_x, pit_pl_y = 0, 0
    spikes_dam = True
    slow = 0
    s = 0
    spkAt_c, spkAt_d, spkAt_x = 0, 0, 508
    coinR = random.randint(7000, 13000)
    cop_at_t = 2000
    la, ra = False, False
    bot_at_sp = 0
    bulAt_x = 500
    bulAt_y = 500
    bulAt_n = 0
    bulAt_c = 0
    bulAt_d = 0
    LINE = False
    tar_c = 0
    tar = False
    SH = 0
    helpp = False
    cdd = 0
    coins_old = 0
#Классы, по названиям все понятно
#Все переменные у меня глобальные, поэтому в начале каждого класса огромный global
    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = player_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def update(self):
            global keys, Flip, player_img, flip, hp, up, down, left, right, i, UP, DOWN, RIGHT, LEFT, blur_img, push, resW, resS, resA, scal, oil_img, shake, FLIP, cop_stop, cop_attack, cop_hp, resD, D, A, FPS, all_sprites, s, slow
            keys = pygame.key.get_pressed()
            if not pause and not menu:
                flip = 0
                #Способности
                if slow > 0:
                    s += 1
                if s >= 300:
                    slow -= 1
                    s = 0
                if resW < 1800:
                    resW += 1
                if resS < 3000:
                    resS += 1
                if resD < 600:
                    resD += 1
                if resA < 4800:
                    resA += 1
                if keys[pygame.K_z]:
                    resA, resD, resS, resW = 4800, 600, 3000, 1800
                if keys[pygame.K_d] and resD >= 600:
                    resD = 0
                    D = True
                    all_sprites = pygame.sprite.Group(player)
                    pygame.image.save(screen, 'screen.png')
                    with Image.open("screen.png") as img:
                        img.load()
                    blur_img = img.convert("L")
                    blur_img = blur_img.filter(ImageFilter.FIND_EDGES)
                    blur_img.save("screen.png")
                    blur_img = pygame.image.load('screen.png').convert()
                    
                elif resD >= 130:
                    D = False
                    all_sprites = AS
                if keys[pygame.K_w] and resW >= 1800 and not D:
                    cop_hp -= 5
                    push = 4
                    resW = 0
                    Wrect.width = 10
                    Wrect.height = 10
                if keys[pygame.K_s] and resS >= 3000 and not D:
                    oil.rect.y = self.rect.y - 120
                    oil.rect.x = self.rect.x - 120
                    resS = 0
                    oil_img = pygame.transform.scale(oil_img, (50, 50))
                    oil.__init__(oil.rect.centerx, oil.rect.centery)
                    scal = 50
                if keys[pygame.K_a] and resA >= 4800 and not D:
                    A = -1 
                    resA = 0
                elif resA >= 600:
                    A = 1
                if oil.rect.x <= 200:
                    oil.rect.x = 200
                if oil.rect.right >= 800:
                    oil.rect.right = 800

                if self.rect.y >= 800 or self.rect.bottom <= 0:
                    self.rect.y = 300
                    self.rect.centerx = 508
                    hp -= 5
                if self.rect.x <= 200:
                    self.rect.x += 1
                if self.rect.right >= 800:
                    self.rect.x -= 1
                    #Движение
                if not keys[pygame.K_SPACE] and resD > 30:
                    if not (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
                        if keys[pygame.K_LEFT] and self.rect.x >= 250:
                            if not Flip: #Поворот игрока на 15 градусов в зависимости от направления[1]
                                FLIP = 1
                                flip = 1
                            self.rect.x -= 5 - slow
                            left -= 5 - slow #Инерция[2]
                            if left < 0: left = 0
                            left += 5 - slow
                            if cop.rect.y <= self.rect.bottom and cop.rect.bottom >= self.rect.y + 20 and cop.rect.right >= self.rect.x + 15 + ((cop.rect.y - self.rect.y) / 4) and cop.rect.x <= self.rect.right - 50: #Коллизия (все подобные строчки это коллизия)
                                shake += 2 #Тряска экрана
                                if cop.rect.x >= 250 and not cop_attack: #Сдвиг копа
                                    self.rect.x += 3 + slow
                                    cop.rect.x -= 2 - slow
                                    left = 0
                                    cop_stop = True
                                    for _ in bots: #Коп двигает ботов
                                        if _.rect.x >= 250:
                                            if _.rect.y <= cop.rect.bottom and _.rect.bottom >= cop.rect.y + 20 and _.rect.right >= cop.rect.x + 20 and _.rect.x <= cop.rect.right - 20:
                                                _.rect.x -= 5 + slow
                                        else:
                                            self.rect.x += 5 - slow
                                            cop.rect.x += 5 - slow
                                else:
                                    left = 0
                                    self.rect.x += 5 - slow
                            else: cop_stop = False
                            for i in bots: #Сдвиг ботов
                                if i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 20 and i.rect.right >= self.rect.x + 15 + ((i.rect.y - self.rect.y) / 4) and i.rect.x <= self.rect.right - 50:
                                    i.rect.x -= 1 - slow
                                    self.rect.x += 4 + slow
                                    left = 0
                                    for _ in bots: #Бот двигает бота
                                        if _ != i:
                                            if _.rect.x >= 250:
                                                if _.rect.y + 30 <= i.rect.bottom and _.rect.bottom >= i.rect.y + 30 and _.rect.right >= i.rect.x + 20 and _.rect.x <= i.rect.right - 20:
                                                    _.rect.x -= 5 + slow
                                            else:
                                                self.rect.x += 5 - slow
                                                i.rect.x += 5 - slow
                                    if i.rect.x <= 250:
                                        self.rect.x += 5
                                        i.rect.x += 5
                        #Дальше расписывать не буду, все то же самое
                        elif keys[pygame.K_RIGHT] and self.rect.x <= 660:
                            if not Flip:
                                FLIP = -1
                                flip = -1
                            self.rect.x += 5 - slow
                            right -= 5 - slow
                            if right < 0: right = 0
                            right += 5 - slow
                            if cop.rect.y <= self.rect.bottom and cop.rect.bottom >= self.rect.y + 20 and cop.rect.right >= self.rect.x + 50 and cop.rect.x <= self.rect.right - 15 - ((cop.rect.y - self.rect.y) / 4):
                                if cop.rect.right <= 750 and not cop_attack:
                                    self.rect.x -= 3 + slow
                                    cop.rect.x += 2 - slow
                                    right = 0
                                    cop_stop = True
                                    shake += 2
                                    for _ in bots:
                                        if _.rect.right <= 750:
                                            if _.rect.y <= cop.rect.bottom and _.rect.bottom >= cop.rect.y + 20 and _.rect.right >= cop.rect.x + 20 and _.rect.x <= cop.rect.right - 20:
                                                _.rect.x += 5 - slow
                                        else:
                                            self.rect.x -= 5 - slow
                                            cop.rect.x -= 5 - slow
                                else:
                                    right = 0
                                    self.rect.x -= 5 - slow
                            else: cop_stop = False
                            for i in bots:
                                if i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 20 and i.rect.right >= self.rect.x + 50 and i.rect.x <= self.rect.right - 15 - ((i.rect.y - self.rect.y) / 4):
                                    i.rect.x += 1 - slow
                                    self.rect.x -= 4 + slow
                                    right = 0
                                    for _ in bots:
                                        if _ != i:
                                            if _.rect.right <= 750:
                                                if _.rect.y + 30 <= i.rect.bottom and _.rect.bottom >= i.rect.y + 30 and _.rect.right >= i.rect.x + 20 and _.rect.x <= i.rect.right - 20:
                                                    _.rect.x += 5 - slow
                                            else:
                                                self.rect.x -= 5 - slow
                                                i.rect.x -= 5 - slow
                                    if i.rect.right >= 750:
                                        self.rect.x -= 5 - slow
                                        i.rect.x -= 5 - slow
                        else:
                            flip = 0
                            FLIP = 0
                            Flip = False
                    if keys[pygame.K_UP] and self.rect.y >= 10:
                        self.rect.y -= 5 - slow
                        up -= 5 - slow
                        if up < 0: up = 0
                        up += 5 - slow
                        if cop.rect.y <= self.rect.bottom and cop.rect.bottom >= self.rect.y + 10 and cop.rect.right >= self.rect.x + 20 and cop.rect.x <= self.rect.right - 20:
                            shake += 2
                            if not CoPdOwN and not cop_attack:
                                up = 0
                                cop.rect.y -= 2 - slow
                                self.rect.y += 3 + slow
                            else:
                                up = 0
                                self.rect.y += 5 - slow
                        for i in bots:
                            if i.rect.y <= self.rect.bottom and i.rect.bottom + 10 >= self.rect.y + 10 and i.rect.right >= self.rect.x + 20 and i.rect.x <= self.rect.right - 20:
                                i.rect.y -= 1 - slow
                                self.rect.y += 4 + slow
                                up = 0
                    if keys[pygame.K_DOWN] and self.rect.bottom <= 790:
                        self.rect.y += 5 - slow
                        down -= 5 - slow
                        if down < 0: down = 0
                        down += 5 - slow
                        if cop.rect.y <= self.rect.bottom and cop.rect.bottom >= self.rect.y + 10 and cop.rect.right >= self.rect.x + 20 and cop.rect.x <= self.rect.right - 20:
                            shake += 2
                            if not CoPdOwN and not cop_attack:
                                down = 0
                                cop.rect.y += 2 - slow
                                self.rect.y -= 3 + slow
                            else:
                                down = 0
                                self.rect.y -= 5 - slow
                        for i in bots:
                            if i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 20 and i.rect.x <= self.rect.right - 20:
                                i.rect.y += 1 - slow
                                self.rect.y -= 4 + slow
                    #[2]Инерция, проверка для ее появления, ее появление
                    for i in bots:
                        if up > 0 and (not keys[pygame.K_UP] or up > 5) and self.rect.y >= 10 and not (i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 10 and i.rect.x <= self.rect.right - 10):
                            UP += 1
                    if UP > 0:
                        self.rect.y -= up
                        up -= 0.3
                        UP = 0
                    if not self.rect.y > 10:
                        up = 0
                    for i in bots:
                        if down > 0 and (not keys[pygame.K_DOWN] or down > 5) and self.rect.bottom <= 790 and not (i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 10 and i.rect.x <= self.rect.right - 10):
                            DOWN += 1
                    if DOWN > 0:
                        self.rect.y += down
                        down -= 0.3
                        DOWN = 0
                    if not self.rect.bottom < 790:
                        down = 0
                    for i in bots:
                        if left > 0 and (not keys[pygame.K_LEFT] or left > 5) and self.rect.x >= 250 and not (i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 10 and i.rect.x <= self.rect.right - 10):
                            LEFT += 1
                    if LEFT > 0:
                        self.rect.x -= left
                        left -= 0.5
                        LEFT = 0
                    if not self.rect.x > 250:
                        left = 0
                    for i in bots:
                        if right > 0 and (not keys[pygame.K_RIGHT] or right > 5) and self.rect.x <= 660 and not (i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 10 and i.rect.x <= self.rect.right - 10):
                            RIGHT += 1
                    if RIGHT > 0:
                        self.rect.x += right
                        right -= 0.5
                        RIGHT = 0
                    if not self.rect.x < 660:
                        right = 0
                else:
                    up = 0; down = 0; left = 0; right = 0
                #[1]Поворот
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
                    player_img = pygame.image.load(os.path.join(img_folder, ("pl-" + str(skin) + ".png"))).convert()
                    self.__init__(self.rect.centerx, self.rect.centery)

    class Bot(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = bot_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def update(self):
            global i, hp, r, DMG, _, stop, push, shake, band_list, bot_spawn, move_speed
            if not pause and not menu:
                band_list = []
                push /= 1.03 
                if push <= 1.5:
                    push = 0
                for i in bots: #Для каждого бота выполняется этот кусок кода
                    if i.rect.y < cop.rect.bottom or not (i.rect.bottom + 60 > cop.rect.y): #Выделение свободных полос для ИИ копа
                        if i.rect.x >= 639:
                            band_list.append(3)
                        elif i.rect.x >= 508:
                            band_list.append(2)
                        elif i.rect.x >= 378:
                            band_list.append(1)
                        elif i.rect.right >= 0:
                            band_list.append(0)
                    
                    if i.rect.y >= 800 and bot_spawn: #Спавн ботов (перемещение с низа экрана вверх)
                        i.rect.y = random.randint(-400, -100)
                        r = random.randint(0, 3)
                        if r == 0:
                            i.rect.centerx = 310
                        elif r == 1:
                            i.rect.centerx = 440
                        elif r == 2:
                            i.rect.centerx = 580
                        elif r == 3:
                            i.rect.centerx = 700
                    
                    if not bot_spawn and i.rect.y >= 800:
                        i.rect.x = 3000

                    if i.rect.y <= player.rect.bottom and i.rect.bottom >= player.rect.y and i.rect.right >= player.rect.x + 10 and i.rect.x <= player.rect.right - 10: #Расчет урона
                        DMG += 1
                    if i.rect.y <= player.rect.y + 10 and i.rect.bottom >= player.rect.y + 10 and i.rect.right >= player.rect.x + 20 and i.rect.x <= player.rect.right - 20:
                        i.rect.y -= 4
                        if i.rect.bottom + 20 > player.rect.y:
                            i.rect.y -= 1
                    for _ in bots:
                        if _ != i: #Я сам не знаю что это, но это нужно
                            if i.rect.y <= _.rect.bottom - 50 and i.rect.bottom >= _.rect.y + 10 and i.rect.right >= _.rect.x + 20 and i.rect.x <= _.rect.right - 20 and i.rect.bottom >= 0:
                                i.rect.y -= 4
                            if i.rect.y <= _.rect.bottom - 50 and i.rect.bottom >= _.rect.y + 10 and i.rect.right >= _.rect.x + 20 and i.rect.x <= _.rect.right - 20 and i.rect.bottom <= 0:
                                i.rect.x += 10
                                i.rect.y -= 100
                    if stop > 9:
                        i.rect.y -= 7
                        stop = 0
                    
                    if i.rect.y <= -500:
                        i.rect.x = random.randint(300, 700)
                        i.rect.y = 2000

                    for _ in bots: #Разлет ботов от W
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
                    
                    if cop_attack:
                        if i.rect.right >= cop.rect.x and i.rect.x <= cop.rect.right: #ОТъезд бота от активного копа, чтобы не мешать ему
                            if i.rect.centerx <= cop.rect.centerx:
                                i.rect.x -= 5
                            else:
                                i.rect.x += 5
                self.rect.y += 4 + move_speed
                if DMG > 0: #Урон
                    shake += 1 / len(bots)
                    hp -= 0.02 * A
                    DMG = 0

    class Cop(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = cop_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
        
        def update(self):
            global SH, up, down, left, right, tar, LINE, move_speed, points, coins, dodge, dodge_, cop_band, free_band, CoPdOwN, CoPdOwNN, cop_stun, cop_img, cop_flip, cop_to_plus, cop_to_minus, shake, hp, cop_attack, cop_at_t, bot_spawn, at_c, cenAt_c, cenAt_d, sidAt_s, sidAt_c, spikes_dam, ATTACK, bul_x, bul_y, bul_img, cenAt_x, cenAt_y, spkAt_c, spkAt_d, spkAt_x, bulAt_x, bulAt_y, bulAt_n, bulAt_c, bulAt_d, cop_hp, bot_at_sp
            if not pause and not menu:
                #ИИ копа[3]
                #Очень сложно объяснить, к тому же тут почти ничего нельзя менять
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
                CoPdOwNN = bot_count
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
                    if self.rect.y < 800:
                        cop_hp -= 10
                    cop_img = cop_cr_img
                    self.__init__(self.rect.centerx, self.rect.centery)
                    cop_flip = True
                    shake += 5
                elif not CoPdOwN:
                    if not cop_attack:
                        cop_img = cop_nr_img
                    else:
                        cop_img = cop_at_img
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
                    if not CoPdOwN and not (player.rect.y <= cop.rect.bottom and player.rect.bottom >= cop.rect.y and player.rect.right >= cop.rect.x + 10 and player.rect.x <= cop.rect.right - 10) and not cop_stop and not cop_attack:               
                        for i in bots:
                            if dodge_ == 1 and not (i.rect.y <= cop.rect.bottom - 10 and i.rect.bottom >= cop.rect.y - 60 and i.rect.x >= cop.rect.right + 50):
                                self.rect.x += 10 * dodge_ / bot_count
                            elif dodge_ == -1 and not (i.rect.y <= cop.rect.bottom - 10 and i.rect.bottom >= cop.rect.y - 60 and i.rect.right + 50 <= cop.rect.right):
                                self.rect.x += 10 * dodge_ / bot_count
                    if not CoPdOwN and not cop_attack:
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
                        self.rect.y += 4 + move_speed
                        if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y + 10 and player.rect.right >= self.rect.x + 25 and player.rect.x <= self.rect.right - 25:
                            player.rect.y += 4
                            hp -= 0.1 * A

                    if not CoPdOwN and not cop_stop and not cop_attack:
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
                    #[3]Вот до сюда
                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right and not cop_attack:
                    hp -= 0.05 * A #Урон
                #----------------Атака копа (активное состояние)---------------------------------#
                at_c -= 1
                if keys[pygame.K_c] and at_c <= 0:
                    at_c = 60 #На кнопку С можно искусственно активировать/деактивировать копа
                    if cop_attack:
                        cop_attack = False
                        bot_spawn = True
                    else:
                        for i in bots: #Начало атаки (искусственное)
                            i.rect.y += 1000
                        ATTACK = random.choice(attack_list)
                        cop.rect.y = 800
                        cop_attack = True
                        cop_hp = 100

                if keys[pygame.K_x]: #На кнопку Х можно выбрать атаку
                    ATTACK = input("attack - ")
                if cop_hp <= 0 and cop_attack and self.rect.y >= 800: #Смерть копа
                    cop_attack = False
                    points += 20
                    coins += 5
                    self.rect.y = 10000
                    cop_at_t = random.randint(600, 1800)

                if cop_attack:
                    bot_spawn = False
                    if bot_at_sp >= 900: #Скидывание одного бота раз в 15 секунд (900/60)
                        bots[0].rect.bottom = 1
                        bots[0].rect.x = random.randint(300, 700)
                        bot_at_sp = 0
                    bot_at_sp += 1
                    for i in bots:
                        if (i.rect.y >= 800 or i.rect.bottom <= 0) and i.rect.y <= 2100:
                            i.rect.y += 2000
                    #Атаки (сложно, муторно, держится на соплях, лезть сюда при острой необходимости)
                    if ATTACK == "central":
                        if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                            if cenAt_c >= 90:
                                hp -= 0.05
                            cop_hp -= 0.1

                        if not CoPdOwN: #Этот и подобные[4] куски кода - "стремление" копа к определенной позиции (в данном случае (cenAt_x, cenAt_y))
                            if self.rect.centerx > cenAt_x + 5:
                                self.rect.x -= 3
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.x -= 3
                            elif self.rect.centerx < cenAt_x:
                                self.rect.x += 3
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.x += 3
                            if self.rect.centery > cenAt_y + 5:
                                self.rect.y -= 3
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.y -= 3
                                if self.rect.y > 900:
                                    self.rect.y -= 10
                            if self.rect.centery < cenAt_y:
                                self.rect.y += 3
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.y += 3

                        if random.randint(0, int(1000 + move_speed * 10)) <= 1 and cenAt_c >= 90: #Смена позиции в рандомный момент 
                            cenAt_x = random.randint(400, 600)
                            cenAt_y = random.randint(300, 600)

                        if self.rect.centerx >= cenAt_x - 10 and self.rect.centerx <= cenAt_x + 10 and self.rect.centery <= cenAt_y + 10 and self.rect.centery >= cenAt_y - 10:
                            if cenAt_c < 90:
                                cenAt_c += 1 #Зарядка
                        else:
                            cenAt_c = 0

                        if cenAt_c >= 90:
                            cenAt_d += 1

                        if cenAt_d >= 50:
                            cenAt_d = 0
                            dx = player.rect.centerx - cop.rect.centerx
                            dy = player.rect.centery - cop.rect.centery
                            rads = math.atan2(-dy,dx)
                            rads %= 2 * math.pi #Математические расчеты угла наклона пули
                            degs = math.degrees(rads)
                            bul_img = pygame.image.load(os.path.join(img_folder, 'bl-1.png')).convert()
                            bul_img = pygame.transform.rotate(bul_img, degs - 90)
                            bullet.__init__(self.rect.centerx, self.rect.centery)
                            bul_x = (player.rect.centerx - cop.rect.centerx) / ((math.sqrt((player.rect.centerx - cop.rect.centerx) ** 2 + (player.rect.centery - cop.rect.centery) ** 2)) / 12)
                            bul_y = (player.rect.centery - cop.rect.centery) / ((math.sqrt((player.rect.centerx - cop.rect.centerx) ** 2 + (player.rect.centery - cop.rect.centery) ** 2)) / 12)

                        if cop_hp <= 0:
                            bot_spawn = True
                            CoPdOwN = True
                
                    if ATTACK == "side":
                        if self.rect.y > 960 and not CoPdOwN:
                            self.rect.y -= 10
                        
                        if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                            cop_hp -= 0.1
                        
                        if (sidAt_s == 0 or sidAt_s == 2 or sidAt_s == 4) and not CoPdOwN: 
                            self.rect.y -= 7 #[4]
                            if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                player.rect.y -= 7
                            if self.rect.centerx >= 315:
                                self.rect.x -= 5
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.x -= 5
                            elif self.rect.centerx <= 305:
                                self.rect.x += 5
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.x += 5
                            if sidAt_c >= 30: #Стрельба
                                bul_img = pygame.image.load(os.path.join(img_folder, 'bl-1.png')).convert()
                                bul_img = pygame.transform.rotate(bul_img, -90)
                                bullet.__init__(self.rect.centerx, self.rect.centery)
                                sidAt_c = 0
                            sidAt_c += 1
                            if self.rect.bottom <= 0:
                                sidAt_s += 1 #Переход на другую сторону
                                self.rect.y = 900
                                self.rect.centerx = 700
                                bullet.rect.y = 1000 

                        if (sidAt_s == 1 or sidAt_s == 3 or sidAt_s == 5) and not CoPdOwN:
                            self.rect.y -= 7 #[4]
                            if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                player.rect.y -= 7
                            if self.rect.centerx >= 705:
                                self.rect.x -= 5
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.x -= 5
                            elif self.rect.centerx <= 695:
                                self.rect.x += 5
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.x += 5
                            if sidAt_c >= 30:
                                bul_img = pygame.image.load(os.path.join(img_folder, 'bl-1.png')).convert()
                                bul_img = pygame.transform.rotate(bul_img, 90)
                                bullet.__init__(self.rect.centerx, self.rect.centery)
                                sidAt_c = 0
                            sidAt_c += 1
                            if self.rect.bottom <= 0:
                                if sidAt_s == 5:
                                    self.rect.centerx = 500
                                else:
                                    self.rect.centerx = 310
                                sidAt_s += 1
                                self.rect.y = 900
                                bullet.rect.y = 1000

                        if sidAt_s == 6 and cop_hp > 0:
                            if sidAt_c < 300: #[4]
                                if self.rect.centerx <= 495 or self.rect.centerx >= 505:
                                    if self.rect.centerx < 500:
                                        if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                            player.rect.x += 5
                                        self.rect.x += 5
                                    if self.rect.centerx > 500:
                                        if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                            player.rect.x -= 5
                                        self.rect.x -= 5
                                if self.rect.centery <= 295 or self.rect.centery >= 305:
                                    if self.rect.centery < 500:
                                        if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                            player.rect.y += 5
                                        self.rect.y += 5
                                    if self.rect.centery > 500:
                                        if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                            player.rect.y -= 5
                                        self.rect.y -= 5
                            else:
                                if self.rect.y < 950:
                                    self.rect.y += 5
                                else:
                                    sidAt_s = 0
                            sidAt_c += 1

                        if cop_hp <= 0:
                            sidAt_s = 0
                            bot_spawn = True
                            CoPdOwN = True
                
                    if ATTACK == "spikes":
                        if spkAt_c <= 1500 and not CoPdOwN:
                            if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                hp -= 0.05
                                cop_hp -= 0.1
                            if self.rect.y >= 5:
                                self.rect.y -= 5
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.y -= 5
                            elif self.rect.y <= -5:
                                self.rect.y += 5
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.y += 5
                            else:
                                spkAt_d += 1

                            if self.rect.centerx >= spkAt_x + 3:
                                self.rect.x -= 10
                            elif self.rect.centerx <= spkAt_x - 7:
                                self.rect.x += 10

                            if spkAt_d == 60:
                                spkAt_x = 378 + 130 * random.randint(0, 2)
                                spikes.rect.center = self.rect.center
                                spkAt_d = 0
                                spikes_dam = True
                        elif not CoPdOwN:
                            if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                cop_hp -= 0.1

                            if self.rect.centery >= 405:
                                self.rect.y -= 5
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.y -= 5
                            elif self.rect.centery <= 395:
                                self.rect.y += 5
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.y += 5

                            if self.rect.centerx >= 505:
                                self.rect.x -= 5
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.x -= 5
                            elif self.rect.centerx <= 495:
                                self.rect.x += 5
                                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                    player.rect.x += 5
                            
                            if spkAt_c >= 1800:
                                spkAt_c = 0

                        spkAt_c += 1

                        if cop_hp <= 0:
                            spkAt_c = 0
                            spkAt_d = 0
                            bot_spawn = True
                            CoPdOwN = True

                    if ATTACK == "bull":
                        if not CoPdOwN:
                            if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                cop_hp -= 0.1
                            if bulAt_c < 3 and self.rect.y <= 800:
                                if bulAt_n == 2:
                                    bulAt_d = 1
                                    tar = True
                                    LINE = True
                                    if not (player.rect.y <= cop.rect.bottom + 60 and player.rect.bottom >= cop.rect.y - 60 and player.rect.right >= cop.rect.x - 60 and player.rect.x <= cop.rect.right + 60):
                                        if abs(self.rect.centerx - player.rect.centerx) >= 5:
                                            self.rect.x += (self.rect.x - player.rect.x) / abs(self.rect.x - player.rect.x + 0.1) * -1
                                        if abs(self.rect.centery - player.rect.centery) >= 5:
                                            self.rect.y += (self.rect.y - player.rect.y) / abs(self.rect.y - player.rect.y + 0.1) * -1
                            else:
                                LINE = False
                                tar = False
                                if not (player.rect.y <= cop.rect.bottom and player.rect.bottom >= cop.rect.y and player.rect.right >= cop.rect.x + 10 and player.rect.x <= cop.rect.right - 10):
                                    self.rect.x += (bulAt_x - cop.rect.centerx) / ((math.sqrt((bulAt_x - cop.rect.centerx) ** 2 + (bulAt_y - cop.rect.centery) ** 2)) / 20)
                                    self.rect.y += (bulAt_y - cop.rect.centery) / ((math.sqrt((bulAt_x - cop.rect.centerx) ** 2 + (bulAt_y - cop.rect.centery) ** 2)) / 20)
                                else:
                                    bulAt_c = 0
                                    bulAt_d = 0
                                    self.rect.x -= (bulAt_x - cop.rect.centerx) / ((math.sqrt((bulAt_x - cop.rect.centerx) ** 2 + (bulAt_y - cop.rect.centery) ** 2)) / 20)
                                    self.rect.y -= (bulAt_y - cop.rect.centery) / ((math.sqrt((bulAt_x - cop.rect.centerx) ** 2 + (bulAt_y - cop.rect.centery) ** 2)) / 20)
                                    if (player.rect.centerx - cop.rect.centerx) / ((math.sqrt((player.rect.centerx - cop.rect.centerx) ** 2 + (player.rect.centery - cop.rect.centery) ** 2)) / 20) > 0:
                                        right += (player.rect.centerx - cop.rect.centerx) / ((math.sqrt((player.rect.centerx - cop.rect.centerx) ** 2 + (player.rect.centery - cop.rect.centery) ** 2)) / 15)
                                    else:
                                        left -= (player.rect.centerx - cop.rect.centerx) / ((math.sqrt((player.rect.centerx - cop.rect.centerx) ** 2 + (player.rect.centery - cop.rect.centery) ** 2)) / 15)
                                    if (player.rect.centery - cop.rect.centery) / ((math.sqrt((player.rect.centerx - cop.rect.centerx) ** 2 + (player.rect.centery - cop.rect.centery) ** 2)) / 20) > 0:
                                        down += (player.rect.centery - cop.rect.centery) / ((math.sqrt((player.rect.centery - cop.rect.centery) ** 2 + (player.rect.centerx - cop.rect.centerx) ** 2)) / 15)
                                    else:
                                        up -= (player.rect.centery - cop.rect.centery) / ((math.sqrt((player.rect.centery - cop.rect.centery) ** 2 + (player.rect.centerx - cop.rect.centerx) ** 2)) / 15)
                                    SH += 5
                                    hp -= 5
                                if (abs(self.rect.centerx - bulAt_x) <= 10 and abs(self.rect.centery - bulAt_y) <= 10) or push > 0:
                                    bulAt_c = 0
                                    bulAt_d = 0

                            if bulAt_d == 0:
                                bulAt_n = 0
                                LINE = False
                                tar = False
                                if self.rect.centerx > bulAt_x + 5:
                                    self.rect.x -= 4
                                    if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                        player.rect.x -= 4
                                elif self.rect.centerx < bulAt_x:
                                    self.rect.x += 4
                                    if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                        player.rect.x += 4
                                else:
                                    bulAt_n += 1
                                if self.rect.centery > bulAt_y + 5:
                                    self.rect.y -= 4
                                    if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                        player.rect.y -= 4
                                    if self.rect.y > 900:
                                        self.rect.y -= 10
                                elif self.rect.centery < bulAt_y:
                                    self.rect.y += 4
                                    if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y - 10 and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right:
                                        player.rect.y += 4
                                else:
                                    bulAt_n += 1
                        else:
                            LINE = False
                            tar = False
                            
                        if cop_hp <= 0:
                            bot_spawn = True
                            CoPdOwN = True


                else:
                    if self.rect.bottom <= 800:
                        if cop_at_t == 0:
                            cop_attack = True
                            ATTACK = random.choice(attack_list)
                            cop_hp = 100
                        cop_at_t -= 1

    class Road(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = road_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def update(self):
            global move_speed
            if not pause and not menu:
                self.rect.y += 15 + move_speed
            if not pause and not menu:
                if move_speed < 1:
                    move_speed += 0.05 #Ускорение игры
                else:
                    move_speed += 0.0001
            if self.rect.y >= 0:
                self.rect.y = -1000

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
                self.rect.y += 15 + move_speed
                for i in bots:
                    if i.rect.x <= self.rect.right and i.rect.right >= self.rect.x and i.rect.y <= self.rect.bottom - 170 and i.rect.bottom >= self.rect.y:
                        i.rect.y += 11
                
                if self.rect.y >= 800:
                    self.rect.x = 2000

                if scal < 300:
                    scal += 10 #Увеличение масла

                oil_img = pygame.image.load(os.path.join(img_folder, 'oi-1.png')).convert()
                oil_img = pygame.transform.scale(oil_img, (scal, scal))
                self.__init__(self.rect.centerx, self.rect.centery)

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = bul_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def update(self):
            global ATTACK, hp, shake, left, right, up, down, SH
            if not pause and not menu:
                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y and player.rect.right >= self.rect.x + 10 and player.rect.x <= self.rect.right - 10:
                    self.rect.x = -1000
                    self.rect.y = -1000
                    hp -= 3
                    SH += 3
                    if ATTACK == "side":
                        if sidAt_s == 0 or sidAt_s == 2 or sidAt_s == 4:
                            right += 10
                        else: left += 10
                    if ATTACK == "central":
                        if bul_x < 0:
                            left += -1 * bul_x / 2
                        else:
                            right += bul_x / 2
                        if bul_y < 0:
                            up += -1 * bul_y / 2
                        else:
                            down += bul_y / 2
                if ATTACK == "central":
                    self.rect.x += bul_x
                    self.rect.y += bul_y
                if ATTACK == "side":
                    self.rect.x += 24 * (1 + -2 * (sidAt_s % 2))

    class Pit(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pit_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def update (self):
            global pit_c, hp, pit_pl_x, pit_pl_y, pit_img, left, right
            if not pause and not menu:
                #Сюда тоже лучше не лезть, яма появляется, если ты долго не двигаешься по х
                if player.rect.x == pit_pl_x:
                    pit_c += 1
                else:
                    pit_c = 0
                    pit_pl_x = player.rect.x
                if pit_c == int(600 - move_speed * 15):
                    pit_img = pygame.image.load(os.path.join(img_folder, 'pt-1.png')).convert()
                    pit_img = pygame.transform.rotate(pit_img, random.randint(0, 360))
                    pit.__init__(player.rect.centerx, -50)
                if pit_c >= int(600 - move_speed * 15) and self.rect.y >= 800:
                    pit_c = 0
                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right and pit_c >= int(600 - move_speed * 15):
                    pit_c = 0
                    hp -= 5
                    if player.rect.x <= 600:
                        right = random.randint(0, 5) + 10
                    else:
                        left = random.randint(0, 5) + 10
                self.rect.y += 15 + move_speed

    class Spikes(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = spikes_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def update (self):
            global SH, hp, left, right, spikes_dam, slow, s
            if not pause and not menu:
                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y and player.rect.right >= self.rect.x and player.rect.x <= self.rect.right and spikes_dam:
                    hp -= 5
                    if slow <= 2:
                        slow += 1
                    s = 0
                    spikes_dam = False #Переключатель для урона от шипов
                    SH += 4
                    if self.rect.centerx >= 500:
                        left += 15
                    else:
                        right += 15

                if push > 0:
                    self.rect.y = 1000

                self.rect.y += 15 + move_speed

    class Coin(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = coin_img
            self.image.set_colorkey(CK)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def update(self):
            global coinR, coins
            if not pause and not menu:
                self.rect.y += 15 + move_speed
                if player.rect.y <= self.rect.bottom and player.rect.bottom >= self.rect.y and player.rect.right >= self.rect.x + 10 and player.rect.x <= self.rect.right - 10:
                    self.rect.y = 800
                    coins += 1
                    coinR = random.randint(int(10000 - (move_speed * 100)), int(15000 - (move_speed * 100)))
                if self.rect.y >= coinR and not cop_attack:
                    self.rect.x = random.randint(300, 700)
                    self.rect.y = -1000

    #Классы -> переменные
    road = Road(500, 0)
    oil = Oil(500, 10000)
    player = Player(508, 700)
    bullet = Bullet(300, 1300)
    cop = Cop(550, 10100)
    pit = Pit(0, 1000)
    spikes = Spikes(260, 1000)
    coin = Coin(random.randint(300, 700), 1000)

    def okrd():
        global dron_img
        (s, e) = functions.okr(player.rect.centerx, player.rect.centery, okr_b)
        dx = s - player.rect.centerx
        dy = e - player.rect.centery
        rads = math.atan2(-dy, dx)
        rads %= 2 * math.pi #Вычисление наклона дрона
        degs = math.degrees(rads)
        dron_img = pygame.image.load(os.path.join(img_folder, 'dr-1.png')).convert()
        dron_img.set_colorkey(CK)
        dron_img = pygame.transform.rotate(dron_img, degs + 90)

    def target(x = player.rect.centerx, y = player.rect.centery, color = (255, 0, 0), r = 7.5):
        global tar_c, bulAt_c, bulAt_y, bulAt_x
        if tar_c <= 10:
            pygame.draw.circle(screen, color, (x, y), tar_c * r, int((10 - tar_c + 1) * 1.5))
            tar_c += 0.15
        else: #Отрисовка эффекта цели
            bulAt_c += 1
            tar_c = -5
            if bulAt_c == 3: bulAt_x = player.rect.centerx; bulAt_y = player.rect.centery

    font_type = pygame.font.Font('Teletactile.ttf', 20)
    font_type_prices = pygame.font.Font('Teletactile.ttf', 10)
    font_type_help = pygame.font.Font(None, 20)
    text = font_type.render((str("Points: ") + str(points)), True, (0, 0, 0))
    textC = font_type.render((str("Coins: ") + str(coins)), True, (0, 0, 0))
    textCO = font_type.render(str(0), True, (0, 0, 0))
    textP = font_type_prices.render((str("  0") + str("C")), True, (0, 0, 0))

    all_sprites = pygame.sprite.Group(road, pit, coin, spikes, oil, bullet, cop, player)
    for i in range(0, bot_count):
        b = Bot(500, random.randint(800, 50000))
        bots.append(b)
        all_sprites.add(b)
    AS = all_sprites
    cop_sprite = pygame.sprite.Group(cop)
    player_sprite = pygame.sprite.Group(player)

    sm1 = [sm_11_img, sm_12_img, sm_13_img, sm_14_img] #Дым

    textW = font_type.render((str("W")), True, (0, 0, 0))
    textD = font_type.render((str("D")), True, (0, 0, 0))
    textS = font_type.render((str("S")), True, (0, 0, 0))
    textA = font_type.render((str("A")), True, (0, 0, 0))
    Wrect = key_img.get_rect()
    Wrect.width = 3000
    Wrect.height = 3000
    cop_at_rect = key_img.get_rect()
    cop_at_rect.width = 250
    cop_at_rect.height = 250

    while running:
        clock.tick(FPS)
        cop_at_rect.center = cop.rect.center
        
        if hp > 100: hp = 100

        w = 0
        shake += SH
        SH -= 0.1 #Тряска экрана
        if SH < 0: SH = 0
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
        if hp > 0:
            if not D: all_sprites.update() #Обновление всех спрайтов
            else: pygame.sprite.Group(player).update() #Обновление только игрока (в случае D)
        else:
            DataFile = open("data.txt", "w")
            if points > record:
                record = points
            sk = ""
            for i in SK: #Смерть игрока
                sk += i
            running = False
            DataFile.write((str(record) + "\n" + str(coins) + "\n" + sk))
            DataFile.close()
    #-------------------Отрисовка интерфейса и всего, что не спрайт-------------------------------#
        Wrect.centerx = player.rect.centerx; Wrect.centery = player.rect.centery
        okr_b += 0.03
        if not pause:
            Wrect.width += 70
            Wrect.height += 70
            shake += 3000 / Wrect.width
            if d >= 30 and hp > 0:
                if not pause and not menu:
                    points += 1
                d = 0
                if not menu:
                    text = font_type.render((str("Points: ") + str(points)), True, (0, 0, 0))
                    textC = font_type.render((str("Coins: ") + str(coins)), True, (0, 0, 0))
            else:
                d += 1
        for i in all_sprites:
            i.rect.x += ran
        all_sprites.draw(screen)
        if LINE: pygame.draw.line(screen, (255, 0, 0), (cop.rect.centerx, cop.rect.centery), (player.rect.centerx, player.rect.centery), 3)
        cop_sprite.draw(screen)

        for i in all_sprites:
            i.rect.x -= ran

        
        if coins != coins_old and cdd < -1:
            if coins - coins_old < 0:
                textCO = font_type.render(str(coins - coins_old), True, (0, 0, 0))
            else:
                textCO = font_type.render("+" + str(coins - coins_old), True, (0, 0, 0))
            screen.blit(textCO, (880, 80))
            cdd = 180
        elif cdd >= 0:
            if coins - coins_old < 0:
                textCO = font_type.render(str(coins - coins_old), True, (0, 0, 0))
            else:
                textCO = font_type.render("+" + str(coins - coins_old), True, (0, 0, 0))
            screen.blit(textCO, (880, 80))
        else:
            coins_old = coins

        cdd -= 1

        if not menu:
            if slow > 0:
                if FLIP == 1:
                    screen.blit(spark_img, (player.rect.x + 9, player.rect.y), spark_rect)
                else:
                    screen.blit(spark_img, (player.rect.x - 17, player.rect.y), spark_rect)
            screen.blit(text, (770, 20))
            screen.blit(textC, (770, 50))
            screen.blit(key_img, (10, 10), key_rect)
            okrd()
            if A == -1: screen.blit(dron_img, functions.okr(player.rect.centerx, player.rect.centery, okr_b), dron_rect)
            if cop_attack:
                pygame.draw.rect(screen, "black", (cop.rect.centerx - 53, cop.rect.y - 26, 106, 16))
                pygame.draw.rect(screen, "red", (cop.rect.centerx - 50, cop.rect.y - 23, cop_hp, 10))
                if ATTACK == "central":
                    pygame.draw.arc(screen, "white", cop_at_rect, 0, cenAt_c / 14, 20)
            pygame.draw.rect(screen, "black", (55, 15, 110, 30))
            pygame.draw.rect(screen, "orange", (60, 20, hp, 20))
            pygame.draw.circle(screen, "black", (50, 100), 34)
            if coin.rect.bottom <= 0 and (coin.rect.y // 100) % 3 <= 1: screen.blit(arrow_img, (coin.rect.x - 20, 0), arrow_rect)
            if resW < 1800:
                pygame.draw.circle(screen, "white", (50, 100), resW / 60)
            else:
                pygame.draw.circle(screen, (185, 255, 185), (50, 100), resW / 60)
            screen.blit(textW, (42, 90))
            pygame.draw.circle(screen, "black", (50, 200), 34)
            if resS < 3000:
                pygame.draw.circle(screen, "white", (50, 200), resS / 100)
            else:
                pygame.draw.circle(screen, (185, 255, 185), (50, 200), resS / 100)
            screen.blit(textS, (42, 190))
            pygame.draw.circle(screen, "black", (50, 300), 34)
            if resD < 600:
                pygame.draw.circle(screen, "white", (50, 300), resD / 20)
            else:
                pygame.draw.circle(screen, (185, 255, 185), (50, 300), resD / 20)
            screen.blit(textD, (42, 290))
            pygame.draw.circle(screen, "black", (50, 400), 34)
            if resA < 4800:
                pygame.draw.circle(screen, "white", (50, 400), resA / 160)
            else:
                pygame.draw.circle(screen, (185, 255, 185), (50, 400), resA / 160)
            screen.blit(textA, (42, 390))
            if Wrect.width <= 2000:
                pygame.draw.arc(screen, "white", Wrect, 0, 30, 100)
            if skin == 6:
                player_img = pygame.image.load(os.path.join(img_folder, ("pl-6" + str(d % 2 + 1) + ".png"))).convert()
            if tar and not pause and not D: target(player.rect.centerx, player.rect.centery)
            if D:
                if resD <= 30:
                    pygame.draw.circle(screen, (0, 0, 0), (player.rect.centerx, player.rect.centery), resD * 35) #Вход в D
                else:
                    screen.blit(blur_img, (0, 0), blur_rect)
                player_sprite.draw(screen)
            if resD > 120 and resD < 150:
                pygame.draw.circle(screen, (0, 0, 0), (player.rect.centerx, player.rect.centery), 1000 - (resD - 120) * 70) #Выход из D
                player_sprite.draw(screen)
            

        else:
            text = font_type.render((str("Record: ") + str(record)), True, (0, 0, 0))
            textC = font_type.render((str("Coins: ") + str(coins)), True, (0, 0, 0))
            screen.blit(text, (770, 20))
            screen.blit(textC, (770, 50))
    #--------------------пауза--------------------------------------#
        smd += 1
        if smd >= 15:
            smd = 0
            smc += 1
            if smc >= 4:
                smc = 0
            sm_img = sm1[smc]
        if hp <= 30:
            if FLIP == -1:
                screen.blit(sm_img, (player.rect.x + 30, player.rect.y), sm_rect)
            else:
                screen.blit(sm_img, (player.rect.x, player.rect.y), sm_rect)
    #----------------Кнопки в паузе и меню--------------------------#
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
        """
        if pause or menu: #Помощь
            if ty[0] >= 355 and ty[1] >= 200 and ty[0] <= 355 + 300 and ty[1] <= 270:
                screen.blit(ps_8_img, (355, 200))
                if w == 1:
                    help_screen = tkinter.Tk()
                    help_screen.title("Помощь")
                    help_lbl = tkinter.Label(help_screen, text="Вы едете на гоночном автомобиле по трассе. По пути вам придется уклоняться от других участников дорожного движения,\nускользать от полиции, а если она вас все-таки настигла – драться за жизнь.\nПока вы едете, вы: копите очки, из которых затем составляется ваш рекорд,\nсобираете монеты, за которые можно покупать новые автомобили\n(которые кстати можно переключать в меню), стараетесь проехать как можно дальше.\nНо далеко уехать будет не так просто: вы постепенно набираете скорость,\nа значит  - все вокруг двигается все быстрее и быстрее.\nНе злите полицию – современные полицейские машины\n(представленные в моей игре) оснащены несколькими видами оружия.\nС помощью этого оружия они смогут вас атаковать:\n1.	Центральная атака  - П (полицейская машина) становится в центр дороги и начинает по вам стрелять.\nНе подъезжайте к ней до того, как она не прекратит стрелять!\n2.	Боковая атака – П ездит по боковым полосам и стреляет вбок. Иногда он делает передышку – этим нужно пользоваться.\n3.	Бросок шипов – П занимает позицию повыше и начинает выпускать шипы. От них вполне можно уворачиваться, но для этого нужна сноровка.\n4.	Таран – П усердно преследует вас и норовит протаранить. Если он все же решится – попробуйте остановить время и уклониться.\nКстати о способностях. Они активируются на кнопки клавиатуры и имеют такие функции:\n1.	W – выпускает волну, отталкивающую все, что  есть на дороге, и уничтожающую шипы.\n2.	D – останавливает время. Пока время остановлено, вы можете выехать из сложной ситуации или уклониться от пули.\n3.	S – выпускает пятно масла. Это масло может сломать П или просто расчистить дорогу.\n4.	А – выпускает дрон, который лечит вас от прикосновения к другим машинам.",
                                     font=("Arial Bold", 18))  
                    help_lbl.grid(column=0, row=0)
                    help_screen.mainloop()  
            else:
                screen.blit(ps_81_img, (355, 200))
        """
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
            if keys[pygame.K_SPACE] and SK[skin - 1] == "1":
                menu = False
            if ty[0] >= 355 and ty[1] >= 300 and ty[0] <= 355 + 300 and ty[1] <= 370:
                screen.blit(ps_4_img, (355, 300))
                if w == 1 and SK[skin - 1] == "1":
                    menu = False
            else:
                screen.blit(ps_41_img, (355, 300))
        if menu: #Смена скинов
            if keys[pygame.K_RIGHT] and ra: 
                ra = False
                if skin == skins:
                    skin = 1
                else:
                    skin += 1
                if skin == 4:
                    road_img = pygame.image.load(os.path.join(img_folder, 'rd-2.png')).convert()
                else:
                    road_img = pygame.image.load(os.path.join(img_folder, 'rd-1.png')).convert()
                road.__init__(road.rect.centerx, road.rect.centery)
                player_img = pygame.image.load(os.path.join(img_folder, ("pl-" + str(skin) + ".png"))).convert()
                player.__init__(player.rect.centerx, player.rect.centery)
                textP = font_type_prices.render(" " + str(prices[skin - 1]) + "C", True, (0, 0, 0))
            elif not keys[pygame.K_RIGHT]:
                ra = True
            if ty[0] >= 580 and ty[1] >= 670 and ty[0] <= 580 + 40 and ty[1] <= 670 + 40:
                screen.blit(ps_5_img, (580, 670))
                if w == 1:
                    if skin == skins:
                        skin = 1
                    else:
                        skin += 1
                    if skin == 4:
                        road_img = pygame.image.load(os.path.join(img_folder, 'rd-2.png')).convert()
                    else:
                        road_img = pygame.image.load(os.path.join(img_folder, 'rd-1.png')).convert()
                    if skin == 6:
                        player_img = pygame.image.load(os.path.join(img_folder, ("pl-61.png"))).convert()
                    else:
                        player_img = pygame.image.load(os.path.join(img_folder, ("pl-" + str(skin) + ".png"))).convert()
                    road.__init__(road.rect.centerx, road.rect.centery)
                    player_img = pygame.image.load(os.path.join(img_folder, ("pl-" + str(skin) + ".png"))).convert()
                    player.__init__(player.rect.centerx, player.rect.centery)
                    textP = font_type_prices.render(" " + str(prices[skin - 1]) + "C", True, (0, 0, 0))
            else:
                screen.blit(ps_51_img, (580, 670))
        if menu:
            if keys[pygame.K_LEFT] and la:
                la = False
                if skin == 1:
                    skin = skins
                else:
                    skin -= 1
                player_img = pygame.image.load(os.path.join(img_folder, ("pl-" + str(skin) + ".png"))).convert()
                if skin == 4:
                    road_img = pygame.image.load(os.path.join(img_folder, 'rd-2.png')).convert()
                else:
                    road_img = pygame.image.load(os.path.join(img_folder, 'rd-1.png')).convert()
                road.__init__(road.rect.centerx, road.rect.centery)
                player.__init__(player.rect.centerx, player.rect.centery)
                textP = font_type_prices.render(" " + str(prices[skin - 1]) + "C", True, (0, 0, 0))
            elif not keys[pygame.K_LEFT]:
                la = True
            if ty[0] >= 395 and ty[1] >= 670 and ty[0] <= 395 + 40 and ty[1] <= 670 + 40:
                screen.blit(ps_6_img, (395, 670))
                if w == 1:
                    if skin == 1:
                        skin = skins
                    else:
                        skin -= 1
                    if skin == 4:
                        road_img = pygame.image.load(os.path.join(img_folder, 'rd-2.png')).convert()
                    else:
                        road_img = pygame.image.load(os.path.join(img_folder, 'rd-1.png')).convert()
                    road.__init__(road.rect.centerx, road.rect.centery)
                    player_img = pygame.image.load(os.path.join(img_folder, ("pl-" + str(skin) + ".png"))).convert()
                    player.__init__(player.rect.centerx, player.rect.centery)
                    textP = font_type_prices.render(" " + str(prices[skin - 1]) + "C", True, (0, 0, 0))
            else:
                screen.blit(ps_61_img, (395, 670))
        if menu and SK[skin - 1] == "0":
            if keys[pygame.K_SPACE]:
                if coins >= prices[skin - 1]:
                    coins -= prices[skin - 1]
                    SK[skin - 1] = "1"
                    DataFile = open("data.txt", "w")
                    sk = ""
                    for i in SK:
                        sk += i
                    DataFile.write((str(record) + "\n" + str(coins) + "\n" + sk))
                    DataFile.close()
            if ty[0] >= 483 and ty[1] >= 680 and ty[0] <= 483 + 50 and ty[1] <= 683 + 27:
                screen.blit(ps_7_img, (483, 680))
                screen.blit(textP, (483, 688))
                if w == 1:
                    if coins >= prices[skin - 1]:
                        coins -= prices[skin - 1]
                        SK[skin - 1] = "1"
                        
                        DataFile = open("data.txt", "w")
                        sk = ""
                        for i in SK:
                            sk += i
                        DataFile.write((str(record) + "\n" + str(coins) + "\n" + sk))
                        DataFile.close()
            else:
                screen.blit(ps_71_img, (483, 680))
                screen.blit(textP, (483, 690))
    #----------------------------------------------------------------#
        outro = True
        if outro and ou_r <= 1010:
            pygame.draw.rect(screen, BLACK, (ou_r, 0, 1000, 1000))
            ou_r += 25
    #----------------------------------------------------------------#
        pygame.display.flip()

pygame.quit()
#Неужели это закончилось...
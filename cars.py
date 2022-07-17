import pygame, os, random

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
player_img = pygame.image.load(os.path.join(img_folder, 'pl-1.png')).convert()
road_img = pygame.image.load(os.path.join(img_folder, 'rd-1.png')).convert()
bot_img = pygame.image.load(os.path.join(img_folder, 'bt-1.png')).convert()
key_img = pygame.image.load(os.path.join(img_folder, 'ky-1.png')).convert()
key_img.set_colorkey(CK)
key_rect = key_img.get_rect()
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
res = 0

class Road(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = road_img
        self.image.set_colorkey(CK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += 7
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
        global keys, Flip, player_img, flip, hp, up, down, left, right, i, UP, DOWN, RIGHT, LEFT, push, res
        keys = pygame.key.get_pressed()
        flip = 0
        res -= 1
        if keys[pygame.K_w] and res <= 0:
            push = 4
            res = 180
        if not keys[pygame.K_SPACE]:
            if keys[pygame.K_LEFT] and self.rect.x >= 250:
                if not Flip:
                    flip = 1
                self.rect.x -= 5
                left = 5
                for i in bots:
                    if i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 20 and i.rect.right >= self.rect.x + 20 and i.rect.x <= self.rect.right - 20:
                        i.rect.x -= 5
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
                    flip = -1
                self.rect.x += 5
                right = 5
                for i in bots:
                    if i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 20 and i.rect.right >= self.rect.x + 20 and i.rect.x <= self.rect.right - 20:
                        i.rect.x += 5
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
                Flip = False
            if keys[pygame.K_UP] and self.rect.y >= 50:
                self.rect.y -= 5
                up = 5
                for i in bots:
                    if i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 20 and i.rect.x <= self.rect.right - 20:
                        i.rect.y -= 5
            if keys[pygame.K_DOWN] and self.rect.bottom <= 700:
                self.rect.y += 5
                down = 5
                for i in bots:
                    if i.rect.y <= self.rect.bottom and i.rect.bottom >= self.rect.y + 10 and i.rect.right >= self.rect.x + 20 and i.rect.x <= self.rect.right - 20:
                        i.rect.y += 5
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
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
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
        global i, hp, r, DMG, _, stop, push
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
            if i.rect.y <= player.rect.bottom and i.rect.bottom >= player.rect.y + 10 and i.rect.right >= player.rect.x + 10 and i.rect.x <= player.rect.right - 10:
                DMG += 1
            #if i.rect.y <= -200:
            #    i.rect.x += 10
            #    print(1)
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
            hp -= 0.01
            DMG = 0

font_type = pygame.font.Font('Teletactile.ttf', 20)
text = font_type.render((str("Points: ") + str(points)), True, (0, 0, 0))

road = Road(500, 0)
player = Player(500, 300)
bot1 = Bot(300, 500)
bot2 = Bot(440, -100 + 500)
bot3 = Bot(580, -250 + 500)
bot4 = Bot(700, -400 + 500)
all_sprites.add(road)
all_sprites.add(player)
all_sprites.add(bot1)
all_sprites.add(bot2)
all_sprites.add(bot3)
all_sprites.add(bot4)

bots = [bot1, bot2, bot3, bot4]

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLUE)
    if d >= 30 and hp > 0:
        points += 1
        d = 0
        text = font_type.render((str("Points: ") + str(points)), True, (0, 0, 0))
    else:
        d += 1
    if hp >= 0:
        all_sprites.remove()
        all_sprites.update()
    all_sprites.draw(screen)
    screen.blit(text, (770, 20))
    screen.blit(key_img, (10, 10), key_rect)
    pygame.draw.rect(screen, "black", (55, 15, 110, 30))
    pygame.draw.rect(screen, "orange", (60, 20, hp, 20))
    pygame.display.flip()

pygame.quit()
from time import sleep
from math import atan2
from math import *
import pygame
from random import *

pygame.font.init()
window = pygame.display.set_mode((400, 700))
background = pygame.image.load('ggg (1).jpg')
background = pygame.transform.scale(background, (400, 700))

hp_image = pygame.image.load('hp1.png')
hp_image = pygame.transform.scale(hp_image, (100, 30))
hp_list = ['hp1.png', 'hp2.png', 'hp3.png', 'hp4.png', 'hp5.png', 'hp6.png', 'hp7.png', 'hp8.png', 'hp9.png',
           'hp10.png', 'hp11.png', ]

explosion_list = ['exp00.png', 'exp01.png', 'exp02.png', 'exp03.png', 'exp04.png', 'exp05.png',
                  'exp06.png', 'exp07.png', 'exp08.png']
exp_counter = 0

hp = 0

clock = pygame.time.Clock()


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.width = width
        self.height = height

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Hero(GameSprite):
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.rect.x < 300:
            self.rect.x += self.speed
        elif keys[pygame.K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed
        elif keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
            pygame.mixer.init()
            sound.play()
            self.image = pygame.transform.scale(pygame.image.load("spaceship1.png"), (self.width, self.height))

        else:
            sound.stop()
            self.image = pygame.transform.scale(pygame.image.load("spaceship3.png"), (self.width, self.height))

    def fire(self):
        bullet = Bullets('laser.png', player.rect.centerx-15, player.rect.y, 25, 70, 15)
        bullet1 = Bullets('laser1.png', player.rect.centerx - 40, player.rect.y + 10, 25, 70, 15)
        bullet2 = Bullets('laser1.png', player.rect.centerx + 15, player.rect.y + 10, 25, 70, 15)
        bullets.add(bullet)
        bullets.add(bullet1)
        bullets.add(bullet2)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            self.kill()

    def fire(self):
        bullet = Bulletss('laser1.png', self.rect.centerx-15, self.rect.y + 75, 15, 15, 15, player.rect.x + 50, player.rect.y)
        bulletss.add(bullet)
        angle = bullet.angle_to_turn(bullet.rect.x, bullet.rect.y, player.rect.x, player.rect.y)
        bullet = pygame.transform.rotate(bullet.image, angle)



class Bullets(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


class Bulletss(GameSprite):
    def __init__(self, image, x, y, width, height, speed, targetx, targety ):
        super().__init__(image, x, y, width, height, speed)
        angle = atan2(targety - y, targetx - x)
        self.targetx = cos(angle) * self.speed
        self.targety = sin(angle) * self.speed

    def update(self):
        self.rect.y += self.targety
        self.rect.x += self.targetx
        if self.rect.y > 700:
            self.kill()

    def angle_to_turn(self, x, y, centerx, centery ):
        a = centerx - x
        b = centery - y
        rad = atan2(-b, a)
        rad = rad % (2*pi)
        angle = degrees(rad)
        return angle


font1 = pygame.font.SysFont('Algerian', 35)

player = Hero('spaceship3.png', 100, 100, 100, 100, 5)
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bulletss = pygame.sprite.Group()

pygame.mixer.init()
sound = pygame.mixer.Sound("sound.mp3")
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
blaster = pygame.mixer.Sound('blaster.mp3')
explosion = pygame.mixer.Sound('explosion.mp3')

height = 700
y = 0
y1 = -height
w = 0
e = 0
s = 0
counter_score = 0
game = True
while game:
    y += 3
    window.blit(background, (0, y))
    y1 += 3
    window.blit(background, (0, y1))
    if y > height:
        y = -height
    if y1 > height:
        y1 = -height

    if w == 0:
        w = 40
        enemy = Enemy("eee.png", randint(5, 300), 0, 100, 100, randint(1, 3))
        enemies.add(enemy)

    else:
        w -= 2

    for e in enemies:
        if s == 0:
            s = 40
            e.fire()
        else:
            s -= 1
    player.show()
    player.move()
    enemies.draw(window)
    enemies.update()
    window.blit(hp_image, (5, 10))

    bullets.update()
    bullets.draw(window)

    bulletss.update()
    bulletss.draw(window)
    score_txt = font1.render("SCORE: " + str(counter_score), True, (255, 255, 255), )
    window.blit(score_txt, (10, 50))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()
                blaster.play()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            player.fire()
            blaster.play()
            blaster.set_volume(0.2)  # 0.0 - 1.0

    collides = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for c in collides:
        counter_score += 1
        explosion.play()
        e = 0
        for i in range(9):
            if e == 0:
                e = 40
                c.image = pygame.transform.scale(pygame.image.load(explosion_list[i]), (100, 100))
                window.blit(c.image, (c.rect.x, c.rect.y))
            else:
                e -= 1

    if pygame.sprite.spritecollide(player, enemies, True) or pygame.sprite.spritecollide(player, bulletss, True):
        hp += 1
        hp_image = pygame.image.load(hp_list[hp])
        hp_image = pygame.transform.scale(hp_image, (100, 30))
        explosion.play()
        e = 0
        for i in range(9):
            if e == 0:
                e = 40
                bulletss.image = pygame.transform.scale(pygame.image.load(explosion_list[i]), ([100, 100]))
                window.blit(bulletss.image, (player.rect.x, player.rect.y))
            else:
                e -= 1
        if hp == 7:
            hp = 0

    pygame.display.update()
    clock.tick(60)
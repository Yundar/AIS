import pygame
import os
from constants import *
from variables import walls, stars, enemies, img_folder, sprites, bullets
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, player_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 152
        self.speedx = 0
        self.speedy = 0
        self.direction = 'top'

    def update(self):
        self.speedx, self.speedy = 0, 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
            self.change_img('tank_green_left.png')
            self.direction = 'left'
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 8
            self.change_img('tank_green_right.png')
            self.direction = 'right'
        elif keystate[pygame.K_UP]:
            self.speedy = -8
            self.change_img('tank_green_top.png')
            self.direction = 'top'
        elif keystate[pygame.K_DOWN]:
            self.speedy = 8
            self.change_img('tank_green_bot.png')
            self.direction = 'bot'
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        # Проверка на столковение со стенами
        self.collide(walls)

        # Проверка на столкновение с базой
        self.collide(stars)

        # Проверка на столкновение с врагом
        self.collide(enemies)

    def collide(self, obj_list):
        hit_list = pygame.sprite.spritecollide(self, obj_list, False)
        for hit in hit_list:
            if self.speedx > 0:
                self.rect.right = hit.rect.left
            elif self.speedx < 0:
                self.rect.left = hit.rect.right

            if self.speedy > 0:
                self.rect.bottom = hit.rect.top
            elif self.speedy < 0:
                self.rect.top = hit.rect.bottom

    def change_img(self, png):
        self.image = pygame.image.load(os.path.join(img_folder, png)).convert()
        self.image.set_colorkey(WHITE)

    def shoot(self):
        if self.direction == 'top':
            bullet = Bullet(self.rect.centerx, self.rect.top, self.direction)
        elif self.direction == 'bot':
            bullet = Bullet(self.rect.centerx, self.rect.bottom, self.direction)
        elif self.direction == 'right':
            bullet = Bullet(self.rect.right, self.rect.centery, self.direction)
        elif self.direction == 'left':
            bullet = Bullet(self.rect.left, self.rect.centery, self.direction)

        sprites.add(bullet)
        bullets.add(bullet)

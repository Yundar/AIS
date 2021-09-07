import pygame
from constants import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()

        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 0
        self.speedx = 0

        if direction == 'top':
            self.speedy = -12
        elif direction == 'bot':
            self.speedy = 12
        elif direction == 'right':
            self.speedx = 12
        elif direction == 'left':
            self.speedx = -12

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0 or self.rect.bottom > HEIGHT or self.rect.bottom > WIDTH:
            self.kill()

import pygame
from constants import WHITE, SQUARE_SIZE


class Enemy(pygame.sprite.Sprite):
    def __init__(self, row, col, enemy_img):
        pygame.sprite.Sprite.__init__(self)
        self.row = row
        self.col = col
        self.image = enemy_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.rect.centerx = 0
        self.rect.centery = 0
        self.calc_pos()

    def calc_pos(self):
        self.rect.centerx = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.rect.centery = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

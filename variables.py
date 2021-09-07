import pygame
import os

sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
bullets = pygame.sprite.Group()
stars = pygame.sprite.Group()
enemies = pygame.sprite.Group()


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'tank_green_top.png'))
box_img = pygame.image.load(os.path.join(img_folder, 'crate_wood.png'))
star_img = pygame.image.load(os.path.join(img_folder, 'star.png'))
enemy_img = pygame.image.load(os.path.join(img_folder, 'tank_red.png'))

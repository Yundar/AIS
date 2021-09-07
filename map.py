import pygame
from constants import *
from box import Box
from star import Star
from enemy import Enemy
from variables import box_img, star_img, enemy_img, sprites, walls, stars, enemies


class Map():
    def __init__(self):
        self.matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 1],
                       [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
                       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                       [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
                       [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                       [1, 0, 0, 1, 1, 3, 1, 0, 0, 1, 1, 1, 1, 0, 1, 3, 1, 1, 0, 0, 1],
                       [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.map = []
        self.create_map()

    def create_map(self):
        for row in range(ROWS):
            self.map.append([])
            for col in range(COLS):
                if self.matrix[row][col] == 1:
                    self.map[row].append(Box(row, col, box_img.convert()))
                    sprites.add(self.map[row][-1])
                    walls.add(self.map[row][-1])
                elif self.matrix[row][col] == 2:
                    self.map[row].append(Star(row, col, star_img.convert()))
                    sprites.add(self.map[row][-1])
                    stars.add(self.map[row][-1])
                elif self.matrix[row][col] == 3:
                    self.map[row].append(Enemy(row, col, enemy_img.convert()))
                    sprites.add(self.map[row][-1])
                    enemies.add(self.map[row][-1])
                else:
                    self.map[row].append(0)

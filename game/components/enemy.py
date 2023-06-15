import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy_1(Sprite):
    def __init__(self, pos_X, pos_Y):
        super().__init__()
        self.image_size = (40, 60)
        self.image = pygame.transform.scale(ENEMY_1, self.image_size)
        self.rect = self.image.get_rect()
        self.rect.x = pos_X
        self.rect.y = pos_Y
        self.speed_y = random.randrange(1, 10)
        self.speed_x = random.randrange(-5, 5)


    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 25:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 10)
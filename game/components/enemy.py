import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy_1(Sprite):
    def __init__(self, pos_X, pos_Y):
        self.image_size = (40, 60)
        self.image = pygame.transform.scale(ENEMY_1, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.image_size[0]
        self.image_rect.y = self.image_size[1]
        self.enemy_speed = 2
        self.speed_x = 10
        self.pos_X = pos_X
        self.pos_Y = pos_Y

    def update(self):
        self.move_y()
        self.move_x()

    def move_y(self):
        self.pos_Y += self.enemy_speed
        if self.pos_Y >= SCREEN_HEIGHT:
            self.pos_Y = SCREEN_HEIGHT
            self.pos_X = (random.randint(20,SCREEN_WIDTH - 40))
            return True

    def move_x(self):
        self.pos_X += self.speed_x
        if self.pos_X < 0:
            self.speed_x += 1
        if self.pos_X > SCREEN_WIDTH - 40:
            self.speed_x -= 1
        

    def draw(self, screen):
        screen.blit(self.image, (self.pos_X, self.pos_Y))
        
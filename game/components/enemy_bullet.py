import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET_ENEMY, SCREEN_WIDTH

class Enemy_Bullet(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_size = (20, 30)
        self.image = pygame.transform.scale(BULLET_ENEMY, self.image_size)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.bullet_speed = 15

    def update(self):
        self.rect.y += self.bullet_speed
        if self.rect.right > SCREEN_WIDTH:
            self.kill()
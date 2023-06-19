import pygame
from pygame.sprite import Sprite
from game.utils.constants import STAR, SCREEN_HEIGHT

class PowerUP_Star(Sprite):
    def __init__(self, x):
        super().__init__()
        self.image_size = (50, 50)
        self.image = pygame.transform.scale(STAR, self.image_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
            self.kill()
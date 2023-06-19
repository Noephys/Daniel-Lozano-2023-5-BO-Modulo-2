import pygame
from pygame.sprite import Sprite
from game.utils.constants import HEART, SCREEN_WIDTH, SCREEN_HEIGHT

class Heart(Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image_size = (30, 30)
        self.image = pygame.transform.scale(HEART, self.image_size)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
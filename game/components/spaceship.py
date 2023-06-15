import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

# casi Todo en pygame es un objeto
# Un personaje en mi juego es un objeto (instancia de algo)
# La nave (spaceship) es un personaje => necesito una clase


# SpaceShip es una clase derivada (hija) de Sprite

# spaceship tiene una "imagen"
class SpaceShip(Sprite):
    
    def __init__(self):
        super().__init__()
        self.image_size = (40, 60)
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.ship_speed = 0


    def update(self):
        self.ship_speed = 0
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.ship_speed = -10
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.ship_speed = 10
        self.rect.x += self.ship_speed
        if self.rect.x >= SCREEN_WIDTH:
            self.rect.x = 1
        if self.rect.x <= 0:
            self.rect.x = SCREEN_WIDTH
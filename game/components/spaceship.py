import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SPACESHIP_SHIELD, SCREEN_WIDTH, SCREEN_HEIGHT

class SpaceShip(Sprite):
    
    def __init__(self):
        super().__init__()
        self.image_size = (40, 60)
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.ship_speed = 0
        self.life = 5
        self.not_shield = True

    def update(self):
        self.ship_speed = 0
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.ship_speed = -5
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.ship_speed = 5
        self.rect.centerx += self.ship_speed
        if self.rect.centerx >= SCREEN_WIDTH:
            self.rect.centerx = 1
        if self.rect.centerx <= 0:
            self.rect.centerx = SCREEN_WIDTH

    def change_image(self): 
        if self.not_shield:
            self.image_size = (40, 60)
            self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        else:
            self.image_size = (75, 65)
            self.image = pygame.transform.scale(SPACESHIP_SHIELD, self.image_size)
        
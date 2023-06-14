import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH

# casi Todo en pygame es un objeto
# Un personaje en mi juego es un objeto (instancia de algo)
# La nave (spaceship) es un personaje => necesito una clase


# SpaceShip es una clase derivada (hija) de Sprite

# spaceship tiene una "imagen"
class SpaceShip(Sprite):
    
    def __init__(self):
        self.image_size = (40, 60)
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.image_size[0]
        self.image_rect.y = self.image_size[1]
        self.ship_speed = 10
        self.image_pos_X = 550


    def update(self):
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        elif user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()

    def move_left(self):
        self.image_pos_X -= self.ship_speed
        if self.image_pos_X <= 0:
            self.image_pos_X = SCREEN_WIDTH

    def move_right(self):
        self.image_pos_X += self.ship_speed
        if self.image_pos_X >= SCREEN_WIDTH:
            self.image_pos_X = 0


    def draw(self, screen):
        screen.blit(self.image, (self.image_pos_X, 530))

        
import pygame
from pygame.sprite import Sprite

from game.utils.constants import PLAYER_EXPLOSION_ANIM

class Player_Explosion(Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = pygame.transform.scale(PLAYER_EXPLOSION_ANIM[0], (20, 30))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(PLAYER_EXPLOSION_ANIM):
                self.kill()
            else:
                center = self.rect.center
                self.image = PLAYER_EXPLOSION_ANIM[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
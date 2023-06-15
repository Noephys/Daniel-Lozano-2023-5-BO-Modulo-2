import pygame
import random

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE

from game.components.spaceship import SpaceShip
from game.components.enemy import Enemy_1
from game.components.bullet import Bullet

all_sprites = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

# Game tiene un "Spaceship" - Por lo general esto es iniciliazar un objeto Spaceship en el __init__
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False  # variable de control para salir del ciclo
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0

        # Game tiene un "Spaceship"
        self.spaceship = SpaceShip()
        all_sprites.add(self.spaceship)

        for x in range(20):
            self.spawn()

    def shoot(self):
        bullet = Bullet((self.spaceship.rect.centerx), (self.spaceship.rect.top))
        all_sprites.add(bullet)
        bullet_list.add(bullet)

    def hit(self):
        hits = pygame.sprite.groupcollide(enemy_list, bullet_list, True, True)
        for hit in hits:
            self.spawn()

    def spawn(self):
        self.enemy = Enemy_1(random.randrange(SCREEN_WIDTH - 40), random.randrange(-100, -40))
        all_sprites.add(self.enemy)
        enemy_list.add(self.enemy)

    def run(self):
        # Game loop: events - update - draw
        self.playing = True

        # while self.playing == True
        while self.playing: # Mientras el atributo playing (self.playing) sea true "repito"
            self.handle_events()
            self.update()
            self.draw()
        else:
            print("Something ocurred to quit the game!!!")
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        # Para un "event" (es un elemento) en la lista (secuencia) que me retorna el metodo get()
        for event in pygame.event.get():
            # si el "event" type es igual a pygame.QUIT entonces cambiamos playing a False
            if event.type == pygame.QUIT:
                self.playing = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shoot()

    def update(self):
        # pass
        all_sprites.update()
        self.hit()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()


        # dibujamos el objeto en pantalla
        all_sprites.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
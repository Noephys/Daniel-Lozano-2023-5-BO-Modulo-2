import pygame
import random
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from game.components.spaceship import SpaceShip
from game.components.enemy import Enemy_1
from game.components.bullet import Bullet
from game.components.enemy_bullet import Enemy_Bullet

all_sprites = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
bullet_enemy_list = pygame.sprite.Group()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0

        self.cadence_enemy_shot = 0

        self.spaceship = SpaceShip()
        all_sprites.add(self.spaceship)

        for x in range(10):
            self.spawn()

    def shoot(self):
        bullet = Bullet((self.spaceship.rect.centerx), (self.spaceship.rect.top))
        bullet_list.add(bullet)
        all_sprites.add(bullet)

    def shoot_enemy(self):
        bullet_enemy = Enemy_Bullet((self.spaceship.rect.centerx), (self.spaceship.rect.bottom))
        bullet_enemy_list.add(bullet_enemy)
        all_sprites.add(bullet_enemy)        

    def hit(self):
        hits = pygame.sprite.groupcollide(enemy_list, bullet_list, True, True)
        for hit in hits:
            self.spawn()

    def spawn(self):
        self.enemy = Enemy_1(random.randrange(SCREEN_WIDTH - 40), random.randrange(-100, -40))
        all_sprites.add(self.enemy)
        enemy_list.add(self.enemy)

    def run(self):
        self.playing = True

        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
        else:
            print("Something ocurred to quit the game!!!")
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shoot()

    def handle_enemy_events(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.cadence_enemy_shot >= 2000:
            for enemy in enemy_list:
                self.shoot_enemy()
            self.cadence_enemy_shot = current_time

    def shoot_enemy(self):
        for enemy in enemy_list:
            bullet_enemy = Enemy_Bullet(enemy.rect.centerx, enemy.rect.bottom)
            bullet_enemy_list.add(bullet_enemy)

    def show_game_over(self):
        self.playing = False                      

    def update(self):
        all_sprites.update()
        bullet_enemy_list.update()
        enemy_list.update()
        self.hit()
        self.handle_events()
        self.handle_enemy_events()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        all_sprites.draw(self.screen)
        bullet_enemy_list.draw(self.screen)
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
import pygame
import random

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, TERMINAL, PLAYER_LASER_SOUND, ENEMY_LASER_SOUND, ENEMY_DESTROY_SOUND, FINALSOUND, LOSE_SOUND, WIN_SOUND, PAUSE_SOUND, START_SOUND, BG_MUSIC, GAMEOVER, YOUWIN

from game.components.spaceship import SpaceShip
from game.components.enemy import Enemy_1
from game.components.bullet import Bullet
from game.components.enemy_bullet import Enemy_Bullet
from game.components.hearts import Heart
from game.components.enemy_explosion import Enemy_Explosion
from game.components.powerup_shield import PowerUP_Shield
from game.components.powerup_heart import PowerUP_Heart
from game.components.powerup_star import PowerUP_Star

pygame.mixer.init()

all_sprites = pygame.sprite.Group()
shield_sprite = pygame.sprite.Group()
heart_sprite = pygame.sprite.Group()
star_sprite = pygame.sprite.Group()
player_list = pygame.sprite.Group()
hearts = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
bullet_enemy_list = pygame.sprite.Group()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0

        self.playing = True
        self.game_over = False
        self.start_menu = True
        self.you_win = False
        self.boolean_shield = False

        self.cadence_enemy_shot = 0
        self.cadence_shield = 0
        self.cadence_star = 0
        self.cadence_heart = 0
        
        self.pos_heart_x = SCREEN_WIDTH - 20

        self.game_try = 0
        self.enemys_destroy = 0
        self.max_score = 0
        self.player_score = 0

        self.spawn_heart()

        self.spaceship = SpaceShip()
        player_list.add(self.spaceship)
        self.additional_hearts = self.spaceship.life

        for x in range(10):
            self.spawn_enemy()

        pygame.mixer.music.load(BG_MUSIC)
        pygame.mixer.music.play(loops=-1)
## ------------------- SPAWNS ----------------------

    def spawn_enemy(self):
        self.enemy = Enemy_1(random.randrange(SCREEN_WIDTH - 40), random.randrange(-100, -40))
        all_sprites.add(self.enemy)
        enemy_list.add(self.enemy)

    def spawn_powerup_shield(self):
        powerup_shield = PowerUP_Shield(random.randrange(30, SCREEN_WIDTH - 30))
        shield_sprite.add(powerup_shield)
        all_sprites.add(powerup_shield)

    def spawn_heart(self):
        heart = Heart((self.pos_heart_x),(SCREEN_HEIGHT - 20))
        hearts.add(heart)

    def spawn_powerup_heart(self):
        powerup_heart = PowerUP_Heart(random.randint(30, SCREEN_WIDTH -30))
        heart_sprite.add(powerup_heart)
        all_sprites.add(powerup_heart)

    def spawn_powerup_star(self):
        powerup_star = PowerUP_Star(random.randint(30, SCREEN_WIDTH -30))
        star_sprite.add(powerup_star)
        all_sprites.add(powerup_star)

## ------------------- SHOOTS ----------------------

    def shoot(self):
        bullet = Bullet((self.spaceship.rect.centerx), (self.spaceship.rect.top))
        bullet_list.add(bullet)
        all_sprites.add(bullet)
        PLAYER_LASER_SOUND.play()

    def shoot_enemy(self):
        for enemy in enemy_list:
            bullet_enemy = Enemy_Bullet(enemy.rect.centerx, enemy.rect.bottom)
            bullet_enemy_list.add(bullet_enemy) 

## ------------------- COLLIDERS ----------------------

    def enemy_hit(self):
        hits = pygame.sprite.groupcollide(enemy_list, bullet_list, True, True)
        for hit in hits:
            self.player_score += 10
            if self.player_score >= 10000:
                self.you_win = True
            self.enemys_destroy += 1
            explosion = Enemy_Explosion(hit.rect.center)
            all_sprites.add(explosion)
            self.spawn_enemy()
            ENEMY_DESTROY_SOUND.play()

    def player_hit(self):
        p_hits = pygame.sprite.groupcollide(bullet_enemy_list, player_list, True, False)
        if p_hits:
            if self.boolean_shield:
                self.spaceship.not_shield = True
                self.spaceship.change_image()
                self.boolean_shield = False
            else:
                self.additional_hearts -= 1
                self.spaceship.life -= 1
                if self.spaceship.life == 0:
                    pygame.mixer.music.set_volume(0)
                    FINALSOUND.play()
                    self.game_over = True

    def powerup_shield_hit(self):
        shield_hit = pygame.sprite.groupcollide(player_list, shield_sprite, False, True)
        if shield_hit:
            self.spaceship.not_shield = False
            self.boolean_shield = True
            self.spaceship.change_image()

    def powerup_heart_hit(self):
        heart_hit = pygame.sprite.groupcollide(player_list, heart_sprite, False, True)
        if heart_hit:
            self.spaceship.life += 1
            self.additional_hearts += 1

    def powerup_star_hit(self):
        star_hit = pygame.sprite.groupcollide(player_list, star_sprite, False, True)
        if star_hit:
            self.player_score += 1000





## ------------------- HANDLES ----------------------

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shoot()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.show_pause_menu()

    def handle_enemy_events(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.cadence_enemy_shot >= 2000:
            ENEMY_LASER_SOUND.play()
            for enemy in enemy_list:
                self.shoot_enemy()
            self.cadence_enemy_shot = current_time

    def handle_spawn_powerup_star(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.cadence_star >= 10000:
            self.spawn_powerup_star()
            self.cadence_star = current_time
    
    def handle_spawn_powerup_shield(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.cadence_shield >= 15000:
            self.spawn_powerup_shield()
            self.cadence_shield = current_time

    def handle_spawn_powerup_heart(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.cadence_heart >= 20000:
            self.spawn_powerup_heart()
            self.cadence_heart = current_time

## ------------------- RUN ----------------------

    def run(self):
        self.playing = True
        self.start_menu = True
        self.game_over = False
        self.you_win = False
        while self.playing:
            if self.start_menu:
                self.show_start_menu()
                self.start_menu = False
            elif self.game_over:
                self.show_go_menu()
                self.game_over = False
            elif self.you_win:
                self.show_win_menu()
                self.you_win = False
            else:
                self.show_game_menu()
        else:
            print("Something ocurred to quit the game!!!")
        pygame.display.quit()
        pygame.quit()

## ------------------- UPDATE ----------------------

    def update(self):
        player_list.update()
        all_sprites.update()
        bullet_enemy_list.update()
        self.powerup_shield_hit()
        self.powerup_heart_hit()
        self.powerup_star_hit()
        self.enemy_hit()
        self.player_hit()
        

## ------------------- DRAW ----------------------

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        all_sprites.draw(self.screen)
        bullet_enemy_list.draw(self.screen)
        player_list.draw(self.screen)
        hearts.draw(self.screen)
        self.draw_text(self.screen, TERMINAL, ("SCORE: "+str(self.player_score)), (135, 180, 0), 20, 100, SCREEN_HEIGHT-20)
        self.draw_text(self.screen, TERMINAL, (str(self.additional_hearts)), (135, 180, 0), 20, SCREEN_WIDTH - 45, SCREEN_HEIGHT-22)
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

    def draw_text(self, screen, font, text, color, size, x, y):
        font_type = pygame.font.Font(font, size)
        surface = font_type.render(text, True, color)
        text_rect = surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(surface, text_rect)

## ------------------- MENUS ----------------------  

    def show_start_menu(self):
        START_SOUND.play()
        PAUSE_SOUND.stop()
        LOSE_SOUND.stop()
        WIN_SOUND.stop()
        pygame.mixer.music.set_volume(0)
        self.draw_background()
        self.draw_text(self.screen, TERMINAL, "SpaceShip", (0, 255, 122), 45, (SCREEN_WIDTH//2), (SCREEN_HEIGHT//4))
        self.draw_text(self.screen, TERMINAL, "The spaceship moves with the keys (A , D) or (<- , ->), and shoots with (SPACE)", (255, 255, 255), 20, (SCREEN_WIDTH//2), (SCREEN_HEIGHT//2))
        self.draw_text(self.screen, TERMINAL, "Press ANY key to start to play", (255, 255, 255), 24, (SCREEN_WIDTH//2), (SCREEN_HEIGHT*0.75))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYUP:
                    waiting = False
    
    def show_go_menu(self):
        pygame.mixer.music.set_volume(0)
        START_SOUND.stop()
        PAUSE_SOUND.stop()
        LOSE_SOUND.play()
        WIN_SOUND.stop()
        self.game_try += 1
        self.spaceship.life = 5
        if self.player_score > self.max_score:
            self.max_score = self.player_score
        self.player_score = 0
        self.draw_background()
        img_size = (200, 200)
        img = pygame.transform.scale(GAMEOVER, img_size)
        img_rect = img.get_rect()
        img_rect.center = ((SCREEN_WIDTH//2),(SCREEN_HEIGHT//4))
        self.screen.blit(img, img_rect)
        self.draw_text(self.screen, TERMINAL, "Try #"+str(self.game_try), (255, 255, 255), 20, (SCREEN_WIDTH//2), (SCREEN_HEIGHT//2))
        self.draw_text(self.screen, TERMINAL, "Max Score: "+str(self.max_score), (255, 255, 255), 20, (SCREEN_WIDTH//2), ((SCREEN_HEIGHT//2) + 30))
        self.draw_text(self.screen, TERMINAL, "Enemies Destroyed: "+str(self.enemys_destroy), (255, 255, 255), 20, (SCREEN_WIDTH//2), ((SCREEN_HEIGHT//2) + 60))
        self.draw_text(self.screen, TERMINAL, "Press 'R' to restart", (255, 255, 255), 20, (SCREEN_WIDTH//2), (SCREEN_HEIGHT * 0.75))
        self.enemys_destroy = 0
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_r:
                        waiting = False
    
    def show_pause_menu(self):
        pygame.mixer.music.set_volume(0)
        START_SOUND.stop()
        PAUSE_SOUND.play()
        LOSE_SOUND.stop()
        WIN_SOUND.stop()
        self.draw_text(self.screen, TERMINAL, "PAUSE", (0, 255, 122), 45, (SCREEN_WIDTH//2), (SCREEN_HEIGHT//4))
        self.draw_text(self.screen, TERMINAL, "Press 'ESC' to continue", (255, 255, 255), 24, (SCREEN_WIDTH//2), (SCREEN_HEIGHT//2))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        waiting = False
    
    def show_game_menu(self):
        START_SOUND.stop()
        PAUSE_SOUND.stop()
        LOSE_SOUND.stop()
        WIN_SOUND.stop()
        pygame.mixer.music.set_volume(0.5)
        self.handle_events()
        self.handle_enemy_events()
        self.handle_spawn_powerup_heart()
        self.handle_spawn_powerup_shield()
        self.handle_spawn_powerup_star()
        self.update()
        self.draw()


    def show_win_menu(self):
        pygame.mixer.music.set_volume(0)
        START_SOUND.stop()
        PAUSE_SOUND.stop()
        LOSE_SOUND.stop()
        WIN_SOUND.play()
        self.game_try += 1
        self.spaceship.life = 5
        if self.player_score > self.max_score:
            self.max_score = self.player_score
        self.player_score = 0
        self.draw_background()
        img_size = (612, 344)
        img = pygame.transform.scale(YOUWIN, img_size)
        img_rect = img.get_rect()
        img_rect.center = ((SCREEN_WIDTH//2),(SCREEN_HEIGHT//4))
        self.screen.blit(img, img_rect)
        self.draw_text(self.screen, TERMINAL, "Try #"+str(self.game_try), (255, 255, 255), 20, (SCREEN_WIDTH//2), (SCREEN_HEIGHT//2))
        self.draw_text(self.screen, TERMINAL, "Your Score: "+str(self.max_score), (255, 255, 255), 20, (SCREEN_WIDTH//2), ((SCREEN_HEIGHT//2) + 30))
        self.draw_text(self.screen, TERMINAL, "Enemies Destroyed: "+str(self.enemys_destroy), (255, 255, 255), 20, (SCREEN_WIDTH//2), ((SCREEN_HEIGHT//2) + 60))
        self.draw_text(self.screen, TERMINAL, "Press 'R' to restart", (255, 255, 255), 20, (SCREEN_WIDTH//2), (SCREEN_HEIGHT * 0.75))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_r:
                        waiting = False
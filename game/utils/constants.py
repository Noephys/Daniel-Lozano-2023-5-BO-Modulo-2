import pygame
import os

pygame.mixer.init()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
FPS = 60
DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(DIR, 'Other/SmallHeart.png'))

STAR = pygame.image.load(os.path.join(DIR, 'Other/Star.png'))


SPACESHIP = pygame.image.load(os.path.join(DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(DIR, "Enemy/enemy_3.png"))
ENEMY_4 = pygame.image.load(os.path.join(DIR, "Enemy/enemy_4.png"))
ENEMY_5 = pygame.image.load(os.path.join(DIR, "Enemy/enemy_5.png"))
ENEMY_6 = pygame.image.load(os.path.join(DIR, "Enemy/enemy_6.png"))
ENEMY_7 = pygame.image.load(os.path.join(DIR, "Enemy/enemy_7.png"))
ENEMY_8 = pygame.image.load(os.path.join(DIR, "Enemy/enemy_8.png"))
ENEMY_9 = pygame.image.load(os.path.join(DIR, "Enemy/enemy_9.png"))
ENEMY_10 = pygame.image.load(os.path.join(DIR, "Enemy/enemy_10.png"))
ENEMY_11 = pygame.image.load(os.path.join(DIR, "Enemy/enemy_11.png"))
ENEMY_12 = pygame.image.load(os.path.join(DIR, "Enemy/enemy_12.png"))

ENEMY_IMAGES = [ENEMY_1, ENEMY_2, ENEMY_3, ENEMY_4, ENEMY_5, ENEMY_6,
                ENEMY_7, ENEMY_8, ENEMY_9, ENEMY_10, ENEMY_11, ENEMY_12]

EXPLOSION_0 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-0.png"))
EXPLOSION_1 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-1.png"))
EXPLOSION_2 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-2.png"))
EXPLOSION_3 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-3.png"))
EXPLOSION_4 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-4.png"))
EXPLOSION_5 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-5.png"))
EXPLOSION_6 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-6.png"))
EXPLOSION_7 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-7.png"))
EXPLOSION_8 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-8.png"))
EXPLOSION_9 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-9.png"))
EXPLOSION_10 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-10.png"))
EXPLOSION_11 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-11.png"))
EXPLOSION_12 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-12.png"))
EXPLOSION_13 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-13.png"))
EXPLOSION_14 = pygame.image.load(os.path.join(DIR, "Explosion/explosion-14.png"))

EXPLOSION_ANIM = [EXPLOSION_0, EXPLOSION_1, EXPLOSION_2, EXPLOSION_3, EXPLOSION_4, EXPLOSION_5, 
                  EXPLOSION_6, EXPLOSION_7, EXPLOSION_8, EXPLOSION_9, EXPLOSION_10, EXPLOSION_11, 
                  EXPLOSION_12, EXPLOSION_13, EXPLOSION_14]

FONT_STYLE = 'freesansbold.ttf'

TERMINAL = pygame.font.match_font('terminal')

GAMEOVER = pygame.image.load(os.path.join(DIR, "Other/gameover.png"))
YOUWIN = pygame.image.load(os.path.join(DIR, "Other/you_win.png"))
PARTICLES = pygame.image.load(os.path.join(DIR, "Other/particles.png"))

PLAYER_LASER_SOUND = pygame.mixer.Sound(os.path.join(DIR, "Sound/player_laser_shot.ogg"))
ENEMY_LASER_SOUND = pygame.mixer.Sound(os.path.join(DIR, "Sound/enemy_laser_shot.ogg"))
ENEMY_DESTROY_SOUND = pygame.mixer.Sound(os.path.join(DIR, "Sound/explosion.wav"))
FINALSOUND = pygame.mixer.Sound(os.path.join(DIR, "Sound/risa-malevola.wav"))
PAUSE_SOUND = pygame.mixer.Sound(os.path.join(DIR, "Sound/Pause_sound.ogg"))
START_SOUND = pygame.mixer.Sound(os.path.join(DIR, "Sound/Star_sound.ogg"))
LOSE_SOUND = pygame.mixer.Sound(os.path.join(DIR, "Sound/Lose_sound.ogg"))
WIN_SOUND = pygame.mixer.Sound(os.path.join(DIR, "Sound/Win_sound.ogg"))
BG_MUSIC = os.path.join(DIR, "Sound/Evangelion-Opening.ogg")
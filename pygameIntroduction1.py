import pygame, random

pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300

GAME_BACKGROUND_COLOR = (255,255,255)
WHITE = (255,255,255)
RED = (192, 0, 0)

# create a clock and set the frame rate
clock = pygame.time.Clock()
FPS = 60

# make a greeting
font = pygame.font.SysFont(None, 24, True, True)
greeting = font.render("Supreme", True, WHITE, RED)
greeting_rect = greeting.get_rect()
greeting_rect.center = (250,150)

# set image
player_image = pygame.image.load("theMonster.png")
player_rect = player_image.get_rect()
player_rect.topleft = (400, 150)

# set image
monster_image = pygame.image.load("theMonster.png")
monster_rect = monster_image.get_rect()
monster_rect.topleft = (400, 150)

# set game values
STARTING_PLAYER_VELOCITY = 10
player_velocity = STARTING_PLAYER_VELOCITY
monster_velocity = 10

# set sound
exit_sound = pygame.mixer.Sound("exit.wav")
pygame.mixer.music.load("ftd_background_music.wav")


display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

# 
pygame.mixer.music.play(-1,0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # use the keys to move the monster
    # the following returns a list of booleans letting us know whether or not
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and monster_rect.top > 50:
        monster_rect.y -= monster_velocity
    if keys[pygame.K_DOWN] and monster_rect.bottom < WINDOW_HEIGHT:
        monster_rect.y += monster_velocity

    # move the player
    player_rect.x -= player_velocity

    if player_rect.x < 0:
        exit_sound.play()
        player_rect.x = WINDOW_WIDTH
        player_rect.y = random.randint(50, WINDOW_HEIGHT - 50)
        player_velocity += 1

    display_surface.fill(GAME_BACKGROUND_COLOR)
    display_surface.blit(greeting, greeting_rect)
    display_surface.blit(player_image,player_rect)
    display_surface.blit(monster_image, monster_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
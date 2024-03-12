import pygame
from sys import exit
from settings import *
from utility import get_image
from player import Player
from monster import Monster


pygame.init()

clock = pygame.time.Clock()

screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))

invul = False
elapsed_time = 0


monster_walk_1 = pygame.image.load("ghost_sprite.png").convert_alpha()
monster_walk_2 = pygame.image.load("ghost_sprite_walk.png").convert_alpha()
monster_walk = [monster_walk_1, monster_walk_2]
monster_index = 0 
monster_surf = monster_walk[monster_index] 


monster_rect = monster_surf.get_rect(midbottom=(monster_x, monster_y))

font = pygame.font.Font(None, 25) 

monster_direction = "Left"


game_over = False

player = Player()
menster = Monster()

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()  
            exit()


    elapsed_time += clock.get_time()
    if elapsed_time > 1000:
        invul = False


    if game_over == False:
                
        player.draw(screen)
        player.update

        screen.fill("#000000")

        text = font.render(f"Lives: {player.lives}", False, "#FFFFFF")
        screen.blit(text, (700, 10))

        screen.blit(monster_surf, monster_rect)

        if player .rect.colliderect(monster_rect):
            if not invul:
                player.lives -= 1
                invul = True
                elapsed_time = 0

        if player.lives <= 0:
            game_over = True
    else:
        screen.fill("#1C1B19")
        end = font.render(f"Game over", False, "#FFFFFF")
        screen.blit(end, (335, 280))
    pygame.display.update()  
    clock.tick(60) 
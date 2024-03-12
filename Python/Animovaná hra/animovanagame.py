import pygame
from sys import exit

pygame.init()

clock = pygame.time.Clock()

screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))

invul = False
elapsed_time = 0

def monster_animation():
    global monster_surf, monster_index
    monster_index += 0.1

    if monster_index > len(monster_walk):
        monster_index = 0

    monster_surf = monster_walk[int(monster_index)]

def get_image(sheet, frame_x, frame_y, width, height, scale):
    img = pygame.Surface((width, height)).convert_alpha()
    img.blit(sheet, (0,0), ((frame_x * width), (frame_y * height), width, height)) #vyblije do img cast ze sheetu, pomoci vzorecku zadame co vyriznout a pak blitnout
    img = pygame.transform.scale(img, (width * scale, height * scale))
    img.set_colorkey((0, 0, 0)) #aby se dobre zobrazovala barva, to co je cerne bude pruhledny
    return img

def player_animation(direction):
    global player_index, player_surf
    frame_count = 4

    player_index += 0.1
    if player_index >= frame_count:
        player_index = 0

    player_surf = get_image(player_spritesheet, int(player_index), direction, 15, 16, 3)


player_x = 100
player_y = 200
player_spritesheet = pygame.image.load("woman_brownhair_run.png").convert_alpha()
#player_surf = get_image(player_spritesheet, 0, 0, 16, 16, 4)
player_surf = get_image(player_spritesheet, 0, 4, 15, 16, 4) #nacte na zaklade hodnot cast toho obrazku do funkce get_image 
player_rect = player_surf.get_rect(midbottom=(player_x, player_y))


player_index = 0
monster_x = 700
monster_y = 300

monster_walk_1 = pygame.image.load("ghost_sprite.png").convert_alpha()
monster_walk_2 = pygame.image.load("ghost_sprite_walk.png").convert_alpha()
monster_walk = [monster_walk_1, monster_walk_2]
monster_index = 0 
monster_surf = monster_walk[monster_index] 


monster_rect = monster_surf.get_rect(midbottom=(monster_x, monster_y))

lives = 3
font = pygame.font.Font(None, 25) 

monster_direction = "Left"


game_over = False

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()  
            exit()


    elapsed_time += clock.get_time()
    if elapsed_time > 1000:
        invul = False


    if game_over == False:
        key = pygame.key.get_pressed()  
        if key[pygame.K_a] and player_rect.top < 0:
            player_rect.left -= 10
            player_animation(2)
        if key[pygame.K_d]: 
            player_rect.right += 10
            player_animation(3)
        if key[pygame.K_w]:
            player_rect.top -= 10
            player_animation(1)
        if key[pygame.K_s]:
            player_rect.bottom += 10
            player_animation(0)

        if monster_rect.x <= 0:
            monster_direction = "Right"
        elif monster_rect.x >= screen_width - 40:
            monster_direction = "Left"

        if monster_direction == "Left":
            monster_rect.x -= 5
        elif monster_direction == "Right":
            monster_rect.x += 5

        monster_animation()
        

        screen.fill("#000000")

        text = font.render(f"Lives: {lives}", False, "#FFFFFF")
        screen.blit(text, (700, 10))

        screen.blit(player_surf, player_rect)
        screen.blit(monster_surf, monster_rect)

        if player_rect.colliderect(monster_rect):
            if not invul:
                lives -= 1
                invul = True
                elapsed_time = 0

        if lives <= 0:
            game_over = True
    else:
        screen.fill("#1C1B19")
        end = font.render(f"Game over", False, "#FFFFFF")
        screen.blit(end, (335, 280))
    pygame.display.update()  
    clock.tick(60) 
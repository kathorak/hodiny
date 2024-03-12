import pygame
from utility import get_image
from settings import *


class Monster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 300 
        self.y = 500
        self.index = 0
        self.spritesheet = pygame.image.load("/assets/monster/monster_sprite_walk.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 4, 15, 16, 4)
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.direction = "Left"

    def animation(self):
        frame_count = 2
        self.index += 0.1
        if self.index > frame_count:
            self.index = 0

        self.image = get_image(self.spritesheet, int(self.index), 1, 16, 16, 5)

    def update(self):
        if self.rect.x <= 0:
            monster_direction = "Right"
        elif self.rect.x >= screen_width - 50:
            monster_direction = "Left"

        if monster_direction == "Left":
            self.rect.x -= 5
        elif monster_direction == "Right":
            self.rect.x += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)
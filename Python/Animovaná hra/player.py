import pygame
from utility import get_image
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 100 
        self.y = 200
        self.index = 0
        self.spritesheet = pygame.image.load("/assets/player/woman_brownhair_run.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 4, 15, 16, 4)
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.lives = 3

    def animation(self, direction):
        frame_count = 4

        self.index += 0.1
        if self.index >= frame_count:
            self.index = 0

        self.image = get_image(self.spritesheet, int(self.index), direction, 15, 16, 3)


    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= 10
            self.animation(2)
        if key[pygame.K_d]: 
            self.rect.x += 10
            self.animation(3)
        if key[pygame.K_w]:
            self.rect.y -= 10
            self.animation(1)
        if key[pygame.K_s]:
            self.rect.y += 10
            self.animation(0)

        if self.rect.x < 0:
            self.rect.x = screen_width - 10
        elif self.rect.x > screen_width:
            self.rect.x = 10

        if self.rect.y < 0:
            self.rect.y = screen_height - 10
        elif self.rect.y > screen_height:
            self.rect.y = 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)
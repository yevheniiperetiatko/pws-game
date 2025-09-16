import pygame
import math

from random import randint
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(
        self, 
        groups,
        target,
        image_name,
        pos=None,
    ):
        super().__init__(groups)
        
        self.image = pygame.transform.scale(
            pygame.image.load(f'sprites/{image_name}').convert_alpha(),
            (60, 80)
        )

        self.pos = pos if pos is not None else self.get_spawn_position()
        self.rect = pygame.FRect(self.pos, (self.image.get_width(), self.image.get_height()))

        self.direction = pygame.math.Vector2()
        self.speed = 100

        self.target = target

    def get_spawn_position(self) -> tuple:
        return (randint(-300, 0), randint(-300, 0))

    def move(self, dt):
        new_direction = pygame.math.Vector2(
            pygame.math.Vector2(self.target.rect.centerx, self.target.rect.centery) - \
            pygame.math.Vector2(self.rect.centerx, self.rect.centery)
        )
        self.direction = new_direction.normalize() if new_direction else new_direction
        
        self.rect.center += self.direction * self.speed * dt

    def check_collision(self):
        print(self.rect.colliderect(self.target.rect))

    def update(self, dt):
        self.move(dt)
        self.check_collision()
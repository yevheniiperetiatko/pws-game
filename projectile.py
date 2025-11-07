import pygame
import math

from all_sprites import AllSprites

class Projectile(pygame.sprite.Sprite):
    def __init__(self, groups, speed, start_pos, target_pos, offset, damage=10):
        super().__init__(groups)

        self.speed = speed
        self.damage = damage
    
        self.image = pygame.transform.scale(
            pygame.image.load('sprites/orb_projectile.png').convert_alpha(),
            (40, 40)
        )

        self.rect = self.image.get_frect(center=(start_pos))

        self.start_pos = start_pos
        self.target_pos = pygame.math.Vector2(target_pos) - offset

        self.direction = self.target_pos - self.start_pos

        if self.direction.length() != 0:
            self.direction = self.direction.normalize()
        
    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        self.move(dt)

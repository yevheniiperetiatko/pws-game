import pygame
import math

from random import randint
from coin import Coin
from animation import Animation

from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(
        self, 
        groups,
        target,
        image_name,
        speed,
        health,
        damage,
        size,
        name,
        pos=None,
    ):
        super().__init__(groups)

        self.groups = groups

        self.speed = speed
        self.damage = damage

        self.size = size
        self.width = size[0]
        self.height = size[1]

        self.health = health

        self.name = name

        self.state = 'idle'

        self.sprites_group = None
        self.animation_speed = None

        if self.name == 'skeleton':
            self.sprites_group = SKELETON_SPRITES
            self.animation_speed = SKELETON_ANIMATION_SPEED
        elif self.name == 'zombie':
            self.sprites_group = ZOMBIE_SPRITES
            self.animation_speed = ZOMBIE_ANIMATION_SPEED
        elif self.name == 'slime':
            self.sprites_group = SLIME_SPRITES
            self.animation_speed = SLIME_ANIMATION_SPEED

        self.animation = Animation(
            self.state,
            self.animation_speed,
            self.sprites_group,
        )
 
        self.image = self.sprites_group[self.state][self.animation.current_frame]

        self.pos = pos if pos is not None else self.get_spawn_position()
        self.rect = pygame.FRect(self.pos, (self.image.get_width(), self.image.get_height()))

        self.direction = pygame.math.Vector2()
        self.target = target

        self.should_mirror = False

    def on_hit(self, bullet_damage, all_coins):
        self.health -= bullet_damage

        if self.health <= 0:
            all_coins.add(Coin(self.groups, self.rect.center, self.groups.offset))
            self.kill()

    def get_spawn_position(self) -> tuple:
        """
        Method calculates a random spawning position for an enemy. 
        """
        return (randint(-300, 0), randint(-300, 0))

    def move(self, dt):
        self.state = 'walking'
        new_direction = pygame.math.Vector2(
            pygame.math.Vector2(self.target.rect.centerx, self.target.rect.centery) - \
            pygame.math.Vector2(self.rect.centerx, self.rect.centery)
        )
        self.direction = new_direction.normalize() if new_direction else new_direction
        
        self.rect.center += self.direction * self.speed * dt

        # check if the sprite should be mirrored
        if self.direction[0] < 0:
            self.should_mirror = True
        else:
            self.should_mirror = False

    def update(self, dt):
        self.move(dt)

        self.image = self.animation.get_sprite(self.state, self.should_mirror)

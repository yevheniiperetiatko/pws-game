import pygame

from settings import *
from projectile import Projectile
from animation import Animation

class Player(pygame.sprite.Sprite):
    def __init__(
            self, 
            pos, 
            groups,
        ):
        super().__init__(groups)
        
        self.name = 'player'
        self.state = "idle"

        self.animation = Animation(
            self.state,
            PLAYER_ANIMATION_SPEED,
            PLAYER_SPRITES
        )

        self.image = PLAYER_SPRITES[self.state][self.animation.current_frame]

        self.pos = pos

        self.health = PLAYER_HEALTH
        self.coin_amount = 999

        self.rect = pygame.FRect(self.pos, (self.image.get_width(), self.image.get_height()))
        
        self.direction = pygame.math.Vector2()
        self.speed = 500

        self.should_mirror = False
        self.invulnerable = False
        self.invuln_timer = 0.0

    def input(self):
        self.keys = pygame.key.get_pressed()

        x_direction = int(self.keys[pygame.K_d]) - int(self.keys[pygame.K_a])
        y_direction = int(self.keys[pygame.K_s]) - int(self.keys[pygame.K_w])

        self.direction.x = x_direction 
        self.direction.y = y_direction
        self.direction = self.direction.normalize() if self.direction else self.direction

        # mirroring player's sprite depending on its direction 
        if x_direction == 1:
            if self.should_mirror == True:
                self.should_mirror = False
        if x_direction == -1:
            if self.should_mirror == False:
                self.should_mirror = True

    def shoot(self, groups) -> Projectile:
        """
        The func creates a projectile and returns it.
        """ 
        projectile = Projectile(
            groups,
            1500,
            self.rect.center,
            pygame.mouse.get_pos(),
            groups.offset
        )

        return projectile

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        self.input()
        self.move(dt)
        
        if self.direction == [0, 0]:
            self.state = 'idle'
        else:
            self.state = 'walking'
        
        self.image = self.animation.get_sprite(self.state, self.should_mirror)

        

        
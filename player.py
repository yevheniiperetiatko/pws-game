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
        self.coin_amount = 0
        self.mana = PLAYER_MANA

        self.rect = pygame.FRect(self.pos, (self.image.get_width(), self.image.get_height()))
        
        self.direction = pygame.math.Vector2()
        self.speed = PLAYER_SPEED

        self.should_mirror = False
        self.invulnerable = False
        self.invuln_timer = 0.0

        self.make_red_duration = 0
        self.was_hit = False

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

        self.mana -= 8

        return projectile

    def on_hit(self, enemy, audio, dt):
        audio.play('witch_hurt')

        if not self.invulnerable:
            self.make_red_duration = PLAYER_MAKE_RED_DURATION
            self.make_red(self.image)
            
            self.health -= enemy.damage
            self.invulnerable = True
            self.invuln_timer = INVULN_TIME
            
            self.was_hit = True
            
        else:
            self.invuln_timer -= dt
            if self.invuln_timer <= 0:
                self.invulnerable = False
        
        if self.health <= 0: self.kill()

    def make_red(self, sprite):
        self.red_sprite = sprite.copy()
        self.red_sprite.fill((200, 10, 20), special_flags=pygame.BLEND_MULT)
        self.image = self.red_sprite

    def move(self, dt):
        if self.rect.y <= -1960:
            self.rect.y = -1960

        elif self.rect.y >= 2000:
            self.rect.y = 2000
        
        if self.rect.x >= 2376:
            self.rect.x = 2376
        
        elif self.rect.x <= -2444:
            self.rect.x = -2444

        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):        
        if self.mana <= 100:
            self.mana += 0.15

        self.input()
        self.move(dt)
        
        if self.direction == [0, 0]:
            self.state = 'idle'
        else:
            self.state = 'walking'
        
        if self.was_hit:
            self.make_red_duration -= dt

        if self.make_red_duration <= 0:
            self.was_hit = False

        if not self.was_hit:
            self.image = self.animation.get_sprite(self.state, self.should_mirror)

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(
            self, 
            pos, 
            groups
        ):
        super().__init__(groups)
        
        self.image = pygame.transform.scale(
            pygame.image.load('sprites/player.png').convert_alpha(),
            (80, 110)
        )

        self.pos = pos

        self.rect = pygame.FRect(self.pos, (self.image.get_width(), self.image.get_height()))
        
        self.direction = pygame.math.Vector2()
        self.speed = 500

        self.was_flipped = False

    def input(self):
        self.keys = pygame.key.get_pressed()

        x_direction = int(self.keys[pygame.K_d]) - int(self.keys[pygame.K_a])
        y_direction = int(self.keys[pygame.K_s]) - int(self.keys[pygame.K_w])

        self.direction.x = x_direction 
        self.direction.y = y_direction
        self.direction = self.direction.normalize() if self.direction else self.direction

        if x_direction == 1:
            if self.was_flipped == True:
                self.image = pygame.transform.flip(self.image, True, False)
                self.was_flipped = False
        if x_direction == -1:
            if self.was_flipped == False:
                self.image = pygame.transform.flip(self.image, True, False)
                self.was_flipped = True

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        self.input()
        self.move(dt)
        
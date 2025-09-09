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
            (150, 150)
        )
        self.rect = self.image.get_frect(center=pos)
        self.pos = pos

        self.direction = pygame.math.Vector2()
        self.speed = 500

        self.was_flipped = False

    def input(self):
        # TODO: create a better name
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

        # print(int(self.keys[pygame.K_d]) - int(self.keys[pygame.K_a]))

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        self.input()
        self.move(dt)
        
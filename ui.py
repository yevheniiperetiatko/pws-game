
import pygame

pygame.init()

font = pygame.font.Font('fonts/font.ttf', 30)

class Crosshair:
    def __init__(self, offset):
        self.image = pygame.transform.scale(
            pygame.image.load('sprites/crosshair.png').convert_alpha(),
            (60, 60)
        )

        self.pos = pygame.mouse.get_pos()
        self.rect = self.image.get_frect(center=self.pos)
        self.display_surface = pygame.display.get_surface()
        self.offset = offset

    def draw(self):
        self.rect.center = pygame.mouse.get_pos() - self.offset
        self.display_surface.blit(self.image, self.rect.topleft + self.offset)

class CoinCounter:
    def __init__(self, amount):
        self.image = pygame.transform.scale(
            pygame.image.load('sprites/coin_counter.png').convert_alpha(),
            (145, 70)
        )
        
        self.display_surface = pygame.display.get_surface()

        self.amount = amount
        self.coin_amount_pos = (90, 222)

        self.pos = (20, 200)
        self.rect = self.image.get_frect(center=self.pos)
    
    def draw(self):
        self.coin_amount_text = font.render(f'{self.amount}', True, (250, 185, 5))

        self.display_surface.blit(self.image, self.pos)
        self.display_surface.blit(self.coin_amount_text, self.coin_amount_pos)

    def update(self, amount):
        self.amount = amount

class HealthBarFrame:
    def __init__(self):
        self.image = pygame.transform.scale(
            pygame.image.load('sprites/healthbar_frame.png').convert_alpha(),
            (400, 100)
        )

        self.pos = (5, 20)
        self.rect = self.image.get_frect(center=self.pos)
        self.display_surface = pygame.display.get_surface()

    def draw(self):
        self.display_surface.blit(self.image, self.pos)

class ManaBarFrame:
    def __init__(self):
        self.image = pygame.transform.scale(
            pygame.image.load('sprites/manabar_frame.png').convert_alpha(),
            (300, 250)
        )

        self.pos = (2, 17)
        self.rect = self.image.get_frect(center=self.pos)
        self.display_surface = pygame.display.get_surface()

    def draw(self):
        self.display_surface.blit(self.image, self.pos)

class HealthBar:
    def __init__(self):
        self.width = 220 # 220

        self.image = pygame.transform.scale(
            pygame.image.load('sprites/healthbar.png').convert_alpha(),
            (self.width, 20)
        )

        self.pos = (86, 55)
        self.rect = self.image.get_frect(center=self.pos)
        self.display_surface = pygame.display.get_surface()
    
    def draw(self, player_health):
        self.width = player_health * 2.2

        if self.width <= 0:
            self.width = 0

        self.image = pygame.transform.scale(self.image, (self.width, 20))
        self.display_surface.blit(self.image, self.pos)

import pygame

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
    def __init__(self):
        self.image = pygame.transform.scale(
            pygame.image.load('sprites/coin_counter.png').convert_alpha(),
            (130, 70)
        )

        self.pos = (20, 200)
        self.rect = self.image.get_frect(center=self.pos)
        self.display_surface = pygame.display.get_surface()
    
    def draw(self):
        self.display_surface.blit(self.image, self.pos)

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

import pygame

class Crosshair:
    def __init__(self, offset):
        self.image = pygame.transform.scale(
            pygame.image.load(f'sprites/crosshair.png').convert_alpha(),
            (60, 60)
        )

        self.pos = pygame.mouse.get_pos()
        self.rect = self.image.get_frect(center=self.pos)
        self.display_surface = pygame.display.get_surface()
        self.offset = offset

    def draw(self):
        self.rect.center = pygame.mouse.get_pos() - self.offset
        self.display_surface.blit(self.image, self.rect.topleft + self.offset)
        
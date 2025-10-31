import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load('map textures/map.png').convert()
        self.rect = self.image.get_frect(center=pos)
import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, groups, pos, offset):
        super().__init__(groups)
        self.image = pygame.transform.scale(
            pygame.image.load('sprites/coin.png').convert_alpha(),
            (25, 30)
        )

        self.pos = pos
        self.rect = self.image.get_frect(center=self.pos)
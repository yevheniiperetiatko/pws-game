import pygame

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def draw(self, target_pos):
        self.offset.x = -target_pos[0] + self.display_surface.width/2
        self.offset.y = -target_pos[1] + self.display_surface.height/2
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)
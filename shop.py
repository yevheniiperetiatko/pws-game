import pygame
import sys

from random import choice

class Shop:
    def __init__(self, pygame):
        self.pygame = pygame

        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('sprites/shop_menu.png')        
        
        self.x = self.display_surface.get_size()[0] / 2
        self.y = self.display_surface.get_size()[1] / 2
        self.pos = (self.x, self.y)
        self.rect = self.image.get_frect(center=self.pos)

        self.powerups = {
            'damage_boost': (
                "+10% to your damage.",
                pygame.transform.scale(
                    pygame.image.load('sprites/powerups/damage_boost_icon.png').convert_alpha(),
                    (220, 210)
                ),
            ),
            'health_boost': (
                "Regenerate 100% of your health.",
                pygame.transform.scale(
                    pygame.image.load('sprites/powerups/health_boost_icon.png').convert_alpha(),
                    (220, 220)
                )
            ),
            'mana_boost': (
                '+10% to your mana regeneration.',
                pygame.transform.scale(
                    pygame.image.load('sprites/powerups/manaboost_icon.png').convert_alpha(),
                    (220, 210)
                )
            ),
            'speed_boost': (
                '+15% to your speed.',
                pygame.transform.scale(
                    pygame.image.load('sprites/powerups/speed_boost_icon.png').convert_alpha(),
                    (220, 220)
                )
            )
        }

        self.items_positions = (
            (self.x-369, self.y-120),
            (self.x-108, self.y-120),
            (self.x+152, self.y-120)
        )

        self.current_powerups = None

    def get_random_powerups(self):
        current_powerups = []
        for i in range(3):
            current_powerups.append(
                (
                    self.powerups[choice(list(self.powerups.keys()))][1], 
                    self.items_positions[i]
                )
            )

        return current_powerups

    def run(self, crosshair):
        self.current_powerups = self.get_random_powerups()

        closed = False
        while not closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.display_surface.blit(self.image, self.rect)

            # display power ups
            for i in range(3):
                self.display_surface.blit(self.current_powerups[i][0], self.current_powerups[i][1])

            crosshair.draw()
            self.pygame.display.update()
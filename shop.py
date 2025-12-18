import pygame
import sys

from random import choice
from settings import *

class PowerUp:
    def __init__(self, description, image_path, image_size, pos=(0,0)):
        self.description = description
        self.image = pygame.transform.scale(
                        pygame.image.load(image_path).convert_alpha(),
                        image_size
                    )
        self.pos = pos
        self.rect = self.image.get_frect(topleft=self.pos)

    def draw(self, display):
        display.blit(self.image, self.rect)

class Shop:
    def __init__(self, pygame):
        self.pygame = pygame

        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('sprites/shop_menu.png')        
        
        self.x = self.display_surface.get_size()[0] / 2
        self.y = self.display_surface.get_size()[1] / 2
        self.pos = (self.x, self.y)
        self.rect = self.image.get_frect(center=self.pos)

        self.powerups = (
            PowerUp(
                '+10% to your damage.',
                'sprites/powerups/damage_boost_icon.png',
                (220, 210),
            ),
            PowerUp(
                "Regenerate 100% of your health.",
                'sprites/powerups/health_boost_icon.png',
                (220, 220)
            ),
            PowerUp (
                '+10% to your mana regeneration.',
                'sprites/powerups/manaboost_icon.png',
                (220, 210)
            ),
            PowerUp (
                '+15% to your speed.',
                'sprites/powerups/speed_boost_icon.png',
                (220, 220)
            )
        )

        self.displayed_powerups = []

        self.items_positions = (
            (self.x-369, self.y-120),
            (self.x-108, self.y-120),
            (self.x+152, self.y-120)
        )

    def on_powerup_hover(self):
        print('asdsad')

    def run(self, crosshair):
        for pos in self.items_positions:
            random_powerup = None

            while True:
                random_powerup = choice(self.powerups)
                if random_powerup in self.displayed_powerups:
                    continue
                break
            
            self.displayed_powerups.append(random_powerup)
            random_powerup.rect.topleft = pos

        closed = False
        while not closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.display_surface.blit(self.image, self.rect)
            # self.powerups[0].draw(self.display_surface)

            for powerup in self.displayed_powerups:
               powerup.draw(self.display_surface)

            crosshair.draw()
            self.pygame.display.update()

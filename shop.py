import pygame
import sys

from random import choice
from settings import *

from ui import Button

class PowerUp:
    def __init__(self, name, description, image_path, image_size, pos=(0,0)):
        self.name = name
        self.description = description
        self.original_image = pygame.transform.scale(
                        pygame.image.load(image_path).convert_alpha(),
                        image_size
                    )
        self.pos = pos
        self.rect = self.original_image.get_frect(topleft=self.pos)

        self.image_hovered = pygame.transform.scale(self.original_image, (image_size[0]*1.1, image_size[1]*1.1))
        self.image = self.original_image
        
        self.font = pygame.font.Font(FONT_PATH, 50)
        self.text_surface = self.font.render(self.description, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=(960, 720))

    def draw(self, display):
        display.blit(self.image, self.rect)

    def on_hover(self, display_surface):
        self.image = self.image_hovered
        display_surface.blit(self.text_surface, self.text_rect)

    def not_hover(self, display_surface):
        self.image = self.original_image

    def on_click(self):
        # if self.name == "damage_boost":
        #     PROJECTILE_DAMAGE = PROJECTILE_DAMAGE * 1.1
        pass

class Shop:
    def __init__(self, pygame, background):
        self.pygame = pygame
        self.background = background

        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('sprites/shop_menu.png')        
        
        self.x = self.display_surface.get_size()[0] / 2
        self.y = self.display_surface.get_size()[1] / 2
        self.pos = (self.x, self.y)
        self.rect = self.image.get_frect(center=self.pos)

        self.exit_button = Button((self.x + 440, self.y-235), 50, 50, '', 0, (255, 0, 255))

        self.powerups = (
            PowerUp(
                'damage_boost',
                '+10% to your damage.',
                'sprites/powerups/damage_boost_icon.png',
                (220, 210),
            ),
            PowerUp(
                "health_regeneration",
                "Regenerate 100% of your health.",
                'sprites/powerups/health_boost_icon.png',
                (220, 220)
            ),
            PowerUp(
                "mana_regeneration",
                '+10% to your mana regeneration.',
                'sprites/powerups/manaboost_icon.png',
                (220, 210)
            ),
            PowerUp (
                "speed_boost",
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

    def run(self, crosshair):
        self.displayed_powerups = []

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
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for powerup in self.displayed_powerups:
                        if powerup.rect.collidepoint(pygame.mouse.get_pos()):
                            powerup.on_click()
                
                if self.exit_button.is_clicked(event):
                    closed = True

            self.display_surface.blit(self.background.image, self.background.rect)

            self.display_surface.blit(self.image, self.rect)
            for powerup in self.displayed_powerups:
                powerup.draw(self.display_surface)

            for powerup in self.displayed_powerups:
                powerup.draw(self.display_surface)
                if powerup.rect.collidepoint(pygame.mouse.get_pos()):
                    powerup.on_hover(self.display_surface)
                else:
                    powerup.not_hover(self.display_surface)

            crosshair.draw()
            self.pygame.display.update()

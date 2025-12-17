import pygame
import sys

from ui import Button
from animation import Animation
from settings import *

class Menu:
    def __init__(self, pygame):
        self.pygame = pygame
        
        self.state = 'menu_background'

        self.animation = Animation(
            self.state,
            MENU_BACKGROUND_ANIMATION_SPEED,
            MENU_BACKGROUND_SPRITES,
        )
        
        self.image = self.animation.get_sprite(self.state)
        self.rect = self.image.get_frect()
        self.display_surface = pygame.display.get_surface()

        self.play_button = Button(
            (1500, 800),
            300,
            100,
            "PLAY",
            50,
            (185, 163, 247),
        )

        self.quit_button = Button(
            (1500, 920),
            300,
            100,
            "QUIT",
            50,
            (185, 163, 247),
        )

        self.buttons = (self.play_button, self.quit_button)

    def run(self, crosshair):
        while True:
            events = pygame.event.get()   
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                
                for button in self.buttons:
                    if button.is_clicked(event):
                        if button.text == 'PLAY':
                            return
                        if button.text == 'QUIT':
                            pygame.quit()
                            sys.exit()
            
            self.display_surface.blit(self.image, self.rect)

            for button in self.buttons:
                button.draw()

            self.image = self.animation.get_sprite(self.state)
            
            crosshair.draw()
            self.pygame.display.update()

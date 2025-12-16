import pygame
import sys

from ui import Button

class Menu:
    def __init__(self, pygame):
        self.pygame = pygame

        self.play_button = Button(
            (1500, 500),
            300,
            100,
            "PLAY",
            50,
            (150, 250, 255),
        )

        self.quit_button = Button(
            (1500, 650),
            300,
            100,
            "QUIT",
            50,
            (150, 250, 255),
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
            
            for button in self.buttons:
                button.draw()

            crosshair.draw()
            self.pygame.display.update()

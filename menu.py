import pygame
import sys

class Menu:
    def __init__(self, pygame):
        self.pygame = pygame

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            self.pygame.display.update()
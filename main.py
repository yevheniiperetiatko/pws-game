import pygame
import sys

from settings import *
from player import Player
from enemy import Enemy
from projectile import Projectile

class Game():
    def __init__(self):
        pygame.init()
        
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Survivors')
        
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()

        self.player = Player((400, 400), self.all_sprites)

        # generate enemies
        self.enemies = self.generate_enemies()

    def draw_all_rects(self, should_work):
        if not should_work:
            return

        # drawing all rects of sprites
        for sprite in self.all_sprites:
            pygame.draw.rect(self.display_surf, (0, 255, 0), sprite.rect) 

    def generate_enemies(self):
        enemies = pygame.sprite.Group()

        for _ in range(1):
            enemies.add(Enemy(self.all_sprites, self.player, 'skeleton.png', 150))
            enemies.add(Enemy(self.all_sprites, self.player, 'zombie.png', 70))
            enemies.add(Enemy(self.all_sprites, self.player, 'slime.png', 100, width=60, height=50))

        return enemies

    def loop(self):
        while self.running:
            # dt
            dt = self.clock.tick(180) / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # if the player presses LMB spawn a projectile
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    projectile = Projectile(
                        self.all_sprites,
                        700,
                        self.player.rect.center,
                        pygame.mouse.get_pos()
                    )  

            self.display_surf.fill('black')
            self.all_sprites.update(dt)
            
            # drawing 
            self.draw_all_rects(False) # function that displays all the rects
            self.all_sprites.draw(self.display_surf)

            pygame.display.update()
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.loop()

import pygame
import sys

from settings import *
from player import Player
from enemy import Enemy

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
        self.enemies = pygame.sprite.Group()

        for _ in range(10):
            self.enemies.add(Enemy(self.all_sprites, self.player, 'skeleton.png'))
            self.enemies.add(Enemy(self.all_sprites, self.player, 'zombie.png'))

    def draw_all_rects(self):
        # drawing all rects of sprites
        for sprite in self.all_sprites:
            pygame.draw.rect(self.display_surf, (0, 255, 0), sprite.rect) 

    def loop(self):
        while self.running:
            # dt
            dt = self.clock.tick(180) / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display_surf.fill('WHITE')
            self.all_sprites.update(dt)
            
            # drawing 
            self.all_sprites.draw(self.display_surf)
            
            # self.draw_all_rects()

            pygame.display.update()
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.loop()

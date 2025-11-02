import pygame
import sys

from settings import *
from ui import *

from player import Player
from enemy import Enemy
from projectile import Projectile
from all_sprites import AllSprites
from background import Background

class Game():
    def __init__(self):
        pygame.init()
        
        self.display_surf = pygame.display.set_mode((0,0), (pygame.FULLSCREEN))
        pygame.display.set_caption('Survivors')
        pygame.mouse.set_visible(False)
        
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = AllSprites()

        self.background = Background((0,0), self.all_sprites)
        self.player = Player((400,400), self.all_sprites)
        self.crosshair = Crosshair(self.all_sprites.offset)

        # generate enemies
        self.enemies = self.generate_enemies()
        self.bullets = pygame.sprite.Group()

    def draw_all_rects(self, should_work):
        if not should_work:
            return

        # drawing all rects of sprites
        for sprite in self.all_sprites:
            pygame.draw.rect(self.display_surf, (0, 255, 0), sprite.rect) 

    def generate_enemies(self):
        enemies = pygame.sprite.Group()

        for _ in range(100):
            # skeleton spawn
            enemies.add(
               Enemy(self.all_sprites, self.player, 'skeleton.png', 150, health=SKELETON_HEALTH, damage=SKELETON_DAMAGE)
            )
            # zombie spawn
            enemies.add(
                Enemy(self.all_sprites, self.player, 'zombie.png', 70, health=ZOMBIE_HEALTH, damage=ZOMBIE_DAMAGE)
            )
            # slime spawn
            enemies.add(
                Enemy(self.all_sprites, self.player, 'slime.png', 100, width=60, height=50, health=SLIME_HEALTH, damage=SLIME_DAMAGE)
            )

        return enemies

    def handle_enemies_colisions(self):
        collisions = pygame.sprite.groupcollide(self.enemies, self.enemies, False, False)

        for enemy, collided_list in collisions.items():
            for other in collided_list:
                if enemy == other:
                    continue
                
                diff = pygame.math.Vector2(enemy.rect.center) - pygame.Vector2(other.rect.center)
                diff = diff.normalize()

                enemy.rect.center += diff
                other.rect.center -= diff

    def loop(self):
        while self.running:
            # dt
            dt = self.clock.tick(180) / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # if the player presses LMB spawn a projectile. shooting
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    projectile = Projectile(
                        self.all_sprites,
                        700,
                        self.player.rect.center,
                        pygame.mouse.get_pos(),
                        self.all_sprites.offset
                    )

                    self.bullets.add(projectile)
            
            self.all_sprites.update(dt)
            
            # drawing 
            self.draw_all_rects(False) # function that displays all the rects (doesnt work anymore lol) TODO: fix or remove
            self.all_sprites.draw(self.player.rect.center)
            self.crosshair.draw()
            
            # TODO: create a func for this
            for bullet in self.bullets:
                collided_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
                for enemy in collided_enemies:
                    bullet.kill()
                    enemy.health -= bullet.damage

                    if enemy.health <= 0: enemy.kill()

            # collisions between enemies
            self.handle_enemies_colisions()

            # checking collision between an enemy and the player      
            # TODO: create a separate func for this logic      
            player_enemy_collisions = pygame.sprite.spritecollide(self.player, self.enemies, False)
            for enemy in player_enemy_collisions:
                if not self.player.invulnerable:
                    self.player.health -= enemy.damage
                    self.player.invulnerable = True
                    self.player.invuln_timer = INVULN_TIME
                else:
                    self.player.invuln_timer -= dt
                    if self.player.invuln_timer <= 0:
                        self.player.invulnerable = False
                
                if self.player.health <= 0: self.player.kill()

            pygame.display.update()
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.loop()

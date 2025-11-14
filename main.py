import pygame
import sys

from settings import *
from ui import *

from coin import Coin
from player import Player
from enemy import Enemy
from projectile import Projectile
from all_sprites import AllSprites
from background import Background

class Game():
    def __init__(self):
        pygame.init()
        
        # display and mouse
        self.display_surf = pygame.display.set_mode((0,0), (pygame.FULLSCREEN))
        pygame.display.set_caption('Survivors')
        pygame.mouse.set_visible(False)
        
        # time
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.convert_frames()

        self.all_coins = pygame.sprite.Group()
        self.all_sprites = AllSprites()

        self.background = Background((0,0), self.all_sprites)
        self.player = Player((400,400), self.all_sprites)
        
        # hud
        self.crosshair = Crosshair(self.all_sprites.offset)
        self.coin_counter = CoinCounter(self.player.coin_amount)
        self.healthbar_frame = HealthBarFrame()
        self.manabar_frame = ManaBarFrame()
        self.healthbar = HealthBar()

        # TODO: reorganize
        # generate enemies
        self.enemies = self.generate_enemies()
        self.bullets = pygame.sprite.Group()

    def generate_enemies(self):
        enemies = pygame.sprite.Group()

        for _ in range(12):
            # skeleton spawn
            enemies.add(
               Enemy(self.all_sprites, self.player, 'skeleton.png', 150, SKELETON_HEALTH, SKELETON_DAMAGE, SKELETON_SIZE, 'skeleton')
            )
            # zombie spawn
            enemies.add(
                Enemy(self.all_sprites, self.player, 'zombie.png', 70, ZOMBIE_HEALTH, ZOMBIE_DAMAGE, ZOMBIE_SIZE, 'zombie')
            )
            # slime spawn
            enemies.add(
                Enemy(self.all_sprites, self.player, 'slime.png', 100, SLIME_HEALTH, SLIME_DAMAGE, SLIME_SIZE, 'slime')
            )

        return enemies

    def handle_enemies_colisions(self):
        collisions = pygame.sprite.groupcollide(self.enemies, self.enemies, False, False)

        for enemy, collided_list in collisions.items():
            for other in collided_list:
                if enemy == other:
                    continue
                
                # logic to push enemies away from each other
                diff = pygame.math.Vector2(enemy.rect.center) - pygame.Vector2(other.rect.center)
                diff = diff.normalize()

                enemy.rect.center += diff
                other.rect.center -= diff

    def handle_bullet_enemies_collision(self):
        for bullet in self.bullets:
                collided_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
                for enemy in collided_enemies:
                    bullet.kill()
                    enemy.on_hit(bullet.damage, self.all_coins)

    def handle_player_enemies_collision(self, dt):
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
    
    def handle_player_coins_collision(self):
        collided_coins = pygame.sprite.spritecollide(self.player, self.all_coins, False)
        if collided_coins:
            for coin in collided_coins:
                self.player.coin_amount += 1
                coin.kill()
    
    def convert_frames(self):
        frame_groups = (
            PLAYER_SPRITES,
            ZOMBIE_SPRITES,
            SKELETON_SPRITES,
            SLIME_SPRITES
        )
        
        for group in frame_groups:
            for state, frames in group.items():
                for i in range(len(frames)):
                    frames[i] = frames[i].convert_alpha()

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
                    projectile = self.player.shoot(self.all_sprites)
                    self.bullets.add(projectile)
            
            self.all_sprites.update(dt)
            self.coin_counter.update(self.player.coin_amount)
            
            # drawing 
            self.all_coins.draw(self.display_surf)
            self.all_sprites.draw(self.player.rect.center)

            # TODO: dont repeat yourself
            self.coin_counter.draw()
            self.healthbar_frame.draw()
            self.manabar_frame.draw()
            self.crosshair.draw()
            self.healthbar.draw(self.player.health)

            # collision between bullet and enemies
            self.handle_bullet_enemies_collision()

            # collision between enemies
            self.handle_enemies_colisions()

            # checking collision between an enemy and the player      
            self.handle_player_enemies_collision(dt)

            # checking collision between coins and the player
            self.handle_player_coins_collision()

            pygame.display.update()
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.loop()

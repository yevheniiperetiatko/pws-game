import pygame
import sys

from settings import *
from ui import *

from coin import Coin
from player import Player
from enemy import Enemy
from menu import Menu
from projectile import Projectile
from all_sprites import AllSprites
from background import Background
from wave_manager import WaveManager
from audio_manager import AudioManager

class Game():
    def __init__(self):
        pygame.init()

        # display and mouse
        self.display_surf = pygame.display.set_mode((0,0), (pygame.FULLSCREEN))
        pygame.display.set_caption('Wandering Witch')
        pygame.mouse.set_visible(False)
        
        # time
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.convert_frames()

        self.all_coins = pygame.sprite.Group()
        self.all_sprites = AllSprites()

        self.background = Background((0,0), self.all_sprites)
        self.player = Player((400,400), self.all_sprites)

        self.audio = AudioManager()
        
        # hud
        self.menu = Menu(pygame)
        self.crosshair = Crosshair(self.all_sprites.offset)
        self.coin_counter = CoinCounter(self.player.coin_amount)
        self.healthbar_frame = HealthBarFrame()
        self.manabar_frame = ManaBarFrame()
        self.healthbar = HealthBar()
        self.manabar = ManaBar()
        self.watch = Watch()

        # TODO: reorganize

        # generate enemies
        self.bullets = pygame.sprite.Group()

        self.enemies = pygame.sprite.Group()

        self.time_elapsed = 0
        self.enemies_amount = 3
        self.last_spawn_second = -1

    def handle_enemies_colisions(self):
        collisions = pygame.sprite.groupcollide(self.enemies, self.enemies, False, False)

        for enemy, collided_list in collisions.items():
            for other in collided_list:
                if enemy == other:
                    continue
                
                # logic to push enemies away from each other
                diff = pygame.math.Vector2(enemy.rect.center) - pygame.Vector2(other.rect.center)
                if diff.length() != 0:
                    diff = diff.normalize()
                else:
                    diff = pygame.Vector2(0, 0)                

                enemy.rect.center += diff
                other.rect.center -= diff

    def handle_bullet_enemies_collision(self):
        for bullet in self.bullets:
                collided_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
                for enemy in collided_enemies:
                    if enemy.state == 'dying':
                        continue
                    
                    bullet.kill()
                    enemy.on_hit(bullet.damage, self.all_coins)

    def handle_player_enemies_collision(self, dt):
        player_enemy_collisions = pygame.sprite.spritecollide(self.player, self.enemies, False)
        for enemy in player_enemy_collisions:
            if enemy.state == 'dying':
                continue
            
            self.player.on_hit(enemy, self.audio, dt)
    
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
        self.menu.run(self.crosshair)
        self.clock.tick()
        self.wave_manager = WaveManager(self.background.rect.width, self.background.rect.height)

        self.audio.play_music('fight hero.wav')

        while self.running:
            # dt
            dt = self.clock.tick(180) / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # if the player presses LMB spawn a projectile. shooting
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.player.mana >= 10:      
                        projectile = self.player.shoot(self.all_sprites)
                        self.bullets.add(projectile)

            # spawn every n seconds 
            if self.watch.seconds in (0, 20, 40, 60) and self.watch.seconds != self.last_spawn_second:
                self.wave_manager.spawn_enemies(
                    self.all_sprites, 
                    self.player, 
                    self.enemies, 
                    self.enemies_amount
                )

                self.last_spawn_second = self.watch.seconds
                self.enemies_amount += 2

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
            self.manabar.draw(self.player.mana)
            self.watch.draw(dt)

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


import pygame
import random

from settings import *
from enemy import Enemy

class WaveManager:
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height

    def get_spawn_chords(self):
        spawn_positions = [
            (-2600, random.randint(-1500, 2000)),
            (2600, random.randint(-1500, 2000)),
            (random.randint(-1500, 2000), 2121),
            (random.randint(-1500, 2000), -2121)
        ]
        return random.choice(spawn_positions)

    def spawn_enemies(self, all_sprites, player, enemies, enemies_amount):

        for _ in range(enemies_amount):
            enemies.add(
                Enemy(all_sprites, player, 'zombie.png', 90, ZOMBIE_HEALTH, ZOMBIE_DAMAGE, ZOMBIE_SIZE, 'zombie', self.get_spawn_chords())
            )
        
        for _ in range(enemies_amount):
            enemies.add(
                Enemy(all_sprites, player, 'skeleton.png', 110, SKELETON_HEALTH, SKELETON_DAMAGE, SKELETON_SIZE, 'skeleton', self.get_spawn_chords())
            )
        
        for _ in range(enemies_amount):
            enemies.add(
                Enemy(all_sprites, player, 'slime.png', 115, SLIME_HEALTH, SLIME_DAMAGE, SLIME_SIZE, 'slime', self.get_spawn_chords())
            )
        print(len(enemies))
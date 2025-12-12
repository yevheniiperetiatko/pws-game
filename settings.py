import pygame

import os

def load_frames(folder, size=None):
    """
    Automatically loads all .png files from the given folder.
    Returns a list of pygame.Surface frames, optionally scaled to 'size'.
    """

    frames = []

    # List all .png files, sorted by name (so 1.png, 2.png, 3.png stay in order)
    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".png"):
            image = pygame.image.load(os.path.join(folder, filename))

            if size:
                image = pygame.transform.scale(image, size)

            frames.append(image)

    return frames

# enemies health
PLAYER_HEALTH = 100
SLIME_HEALTH = 30
SKELETON_HEALTH = 50 
ZOMBIE_HEALTH = 65

# MANA
PLAYER_MANA = 100

# damages
SLIME_DAMAGE = 5
SKELETON_DAMAGE = 8 
ZOMBIE_DAMAGE = 10
PROJECTILE_DAMAGE = 10

# cooldown after player takes damage
INVULN_TIME = 0.3

# animation speed
PLAYER_ANIMATION_SPEED = 0.025
SKELETON_ANIMATION_SPEED = 0.025
ZOMBIE_ANIMATION_SPEED = 0.03
SLIME_ANIMATION_SPEED = 0.025

# sprites sizes width x height
PLAYER_SIZE = (80, 110)
ZOMBIE_SIZE = (60, 80)
SKELETON_SIZE = (60, 90)
SLIME_SIZE = (75, 50)

# enemy make red duration
ENEMY_MAKE_RED_DURATION = 0.1

# state
game_state = 'menu'

# SPRITES
PLAYER_SPRITES = {
    'idle': load_frames("sprites/player/idle", PLAYER_SIZE),
    'walking': load_frames("sprites/player/walking", PLAYER_SIZE),
    'dying': load_frames("sprites/slime/dying", PLAYER_SIZE),
}

ZOMBIE_SPRITES = {
    'idle': load_frames("sprites/zombie/idle", ZOMBIE_SIZE),
    'walking': load_frames("sprites/zombie/walking", ZOMBIE_SIZE),
    'dying': load_frames("sprites/zombie/dying", ZOMBIE_SIZE),
}

SKELETON_SPRITES = {
    'idle': load_frames("sprites/skeleton/idle", SKELETON_SIZE),
    'walking': load_frames("sprites/skeleton/walking", SKELETON_SIZE),
    'dying': load_frames("sprites/skeleton/dying", SKELETON_SIZE),
}

SLIME_SPRITES = {
    'idle': load_frames("sprites/slime/idle", SLIME_SIZE),
    'walking': load_frames("sprites/slime/walking", SLIME_SIZE),
    'dying': load_frames("sprites/slime/dying", SLIME_SIZE),
}

# waves
waves = {
    1: {
        "zomb_amount": 3,
        "skelet_amount": 3,
        "slime_amount": 3,  
    },
    2: {
        "zomb_amount": 7,
        "skelet_amount": 2,
        "slime_amount": 5,  
    },
    3: {
        "zomb_amount": 16,
        "skelet_amount": 12,
        "slime_amount": 20,  
    },
    4: {
        "zomb_amount": 25,
        "skelet_amount": 25,
        "slime_amount": 25,  
    },
    5: {
        "zomb_amount": 30,
        "skelet_amount": 40,
        "slime_amount": 50,  
    },
    6: {
        "zomb_amount": 50,
        "skelet_amount": 45,
        "slime_amount": 60,  
    },
    7: {
        "zomb_amount": 70,
        "skelet_amount": 60,
        "slime_amount": 70,  
    },
    8: {
        "zomb_amount": 80,
        "skelet_amount": 80,
        "slime_amount": 80,  
    },
    9: {
        "zomb_amount": 99,
        "skelet_amount": 99,
        "slime_amount": 99,  
    },
    10: {
        "zomb_amount": 7,
        "skelet_amount": 2,
        "slime_amount": 5,  
    },

}
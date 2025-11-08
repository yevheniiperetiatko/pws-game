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

WINDOW_WIDTH = 1300# 1920
WINDOW_HEIGHT = 880 # 1080

# enemies health
PLAYER_HEALTH = 100
SLIME_HEALTH = 30
SKELETON_HEALTH = 50 
ZOMBIE_HEALTH = 65

# enemies damage
SLIME_DAMAGE = 5
SKELETON_DAMAGE = 8 
ZOMBIE_DAMAGE = 10

# cooldown after player takes damage
INVULN_TIME = 0.3

# animation speed
PLAYER_ANIMATION_SPEED = 0.03
SKELETON_ANIMATION_SPEED = 0.03
ZOMBIE_ANIMATION_SPEED = 0.03
SLIME_ANIMATION_SPEED = 0.03

# sprites sizes width x height
PLAYER_SIZE = (80, 110)
ZOMBIE_SIZE = (60, 80)
SKELETON_SIZE = (60, 90)
SLIME_SIZE = (75, 50)

# SPRITES
PLAYER_SPRITES = {
    'idle': load_frames("sprites/player/idle", PLAYER_SIZE),
    'walking': load_frames("sprites/player/walking", PLAYER_SIZE),
}

ZOMBIE_SPRITES = {
    'idle': load_frames("sprites/zombie/idle", ZOMBIE_SIZE),
    'walking': load_frames("sprites/zombie/walking", ZOMBIE_SIZE)
}

SKELETON_SPRITES = {
    'idle': load_frames("sprites/skeleton/idle", SKELETON_SIZE),
    'walking': load_frames("sprites/skeleton/walking", SKELETON_SIZE)
}

SLIME_SPRITES = {
    'idle': load_frames("sprites/slime/idle", SLIME_SIZE),
    'walking': load_frames("sprites/slime/walking", SLIME_SIZE)
}

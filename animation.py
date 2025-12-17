
import pygame

class Animation:
    def __init__(self, state, speed, sprites):
        self.sprites = sprites
        self.state = state
        self.current_state = None
        self.current_frame = 0
        self.death_anim_current_frame = 0
        self.speed = speed

    def get_sprite(self, current_state, should_mirror=False):
        """
        This function returns the current frame 
        for animation according to the current state 
        of an entity.
        """

        if self.current_frame > len(self.sprites[current_state]) - 1:
            self.current_frame = 0

        if current_state == 'dying':
            sprite = self.sprites[current_state][int(self.death_anim_current_frame)]
            self.death_anim_current_frame += self.speed
        else:
            sprite = self.sprites[current_state][int(self.current_frame)]

        if should_mirror: sprite = pygame.transform.flip(sprite, True, False)

        self.current_frame += self.speed

        return sprite
        

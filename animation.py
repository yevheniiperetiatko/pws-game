
import pygame

class Animation:
    def __init__(self, state, speed, sprites):
        self.sprites = sprites
        self.state = state
        self.current_frame = 0
        self.speed = speed

    def get_sprite(self, current_state):
        """
        This function returns the current sprite 
        to animate according to the current state 
        of an entity.
        """
        
        if self.current_frame > len(self.sprites[self.state]) - 1:
            self.current_frame = 0

        sprite = self.sprites[self.state][int(self.current_frame)]
        self.current_frame += self.speed

        return sprite
        

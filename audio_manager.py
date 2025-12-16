import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        
        self.sounds = {
            "witch_hurt": pygame.mixer.Sound("sounds/witch_hurt.wav")
        }

        self.sounds['witch_hurt'].set_volume(0.1)

        pygame.mixer.set_num_channels(16)

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].play()
        else:
            print(f'Sound {name} is not found.')

    def play_music(self, song_name, loop=True, volume=0.3):
        pygame.mixer.music.load(f'sounds/music/{song_name}')
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1 if loop else 0)

    def stop_music(self):
        pygame.mixer.music.stop()
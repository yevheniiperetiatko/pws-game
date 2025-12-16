
import pygame

pygame.init()

FONT_PATH = 'fonts/font.ttf'
money_amount_font = pygame.font.Font(FONT_PATH, 30)
watch_time_font = pygame.font.Font(FONT_PATH, 50)

class UIElement:
    def __init__(self, image_path, scale_size, pos):
        self.image = pygame.transform.scale(
            pygame.image.load(f'{image_path}').convert_alpha(),
            scale_size,#(60, 60)
        )

        self.pos = pos
        self.rect = self.image.get_frect(center=self.pos)
        self.display_surface = pygame.display.get_surface()

    def draw(self):
        self.display_surface.blit(self.image, self.pos)

class Crosshair(UIElement):
    def __init__(self, offset):
        super().__init__(
            "sprites/crosshair.png",
            (60, 60),
            pygame.mouse.get_pos(),
        )

        self.offset = offset

    def draw(self):
        self.rect.center = pygame.mouse.get_pos() - self.offset
        self.display_surface.blit(self.image, self.rect.topleft + self.offset)

class CoinCounter(UIElement):
    def __init__(self, amount):
        super().__init__(
            "sprites/coin_counter.png",
            (145, 70),
            (20, 200),
        )

        self.amount = amount
        self.coin_amount_pos = (90, 222)
    
    def draw(self):
        self.coin_amount_text = money_amount_font.render(f'{self.amount}', True, (250, 185, 5))

        self.display_surface.blit(self.image, self.pos)
        self.display_surface.blit(self.coin_amount_text, self.coin_amount_pos)

    def update(self, amount):
        self.amount = amount

class HealthBarFrame(UIElement):
    def __init__(self):
        super().__init__(
            'sprites/healthbar_frame.png',
            (400, 100),
            (5, 20)
        )

class ManaBarFrame(UIElement):
    def __init__(self):
        super().__init__(
            'sprites/manabar_frame.png',
            (300, 250),
            (2, 17)
        )

class HealthBar(UIElement):
    def __init__(self):
        super().__init__(
            'sprites/healthbar.png',
            (220, 20),
            (86, 55)
        )
        
        self.width = 220
    
    def draw(self, player_health):
        self.width = player_health * 2.2

        if self.width <= 0:
            self.width = 0

        self.image = pygame.transform.scale(self.image, (self.width, 20))
        self.display_surface.blit(self.image, self.pos)

class ManaBar(UIElement):
    def __init__(self):
        super().__init__(
            'sprites/manabar.png',
            (159, 20),
            (81, 137)
        )
        self.width = 159

    def draw(self, player_mana):
        self.width = player_mana * 1.62

        if self.width < 0:
            self.width = 0
        
        self.image = pygame.transform.scale(self.image, (self.width, 20))
        self.display_surface.blit(self.image, self.pos)

class Watch:
    def __init__(self):
        self.time_elapsed = 0
        
        self.minutes = 0
        self.seconds = 0

        self.display_surface = pygame.display.get_surface()
        self.pos = (self.display_surface.width / 2.2, 50)

    def draw(self, dt):
        self.time_elapsed += dt
        
        self.minutes = int(self.time_elapsed // 60)
        self.seconds = int(self.time_elapsed % 60)

        if self.seconds >= 10:
            self.seconds_text = str(self.seconds)
        else:
            self.seconds_text = f'0{self.seconds}'

        if self.minutes >= 10:
            self.minutes_text = str(self.minutes)
        else:
            self.minutes_text = f'0{self.minutes}'
        
        self.time_text = watch_time_font.render(f'{self.minutes_text} : {self.seconds_text}', True, (255, 255, 255))

        self.display_surface.blit(self.time_text, self.pos)
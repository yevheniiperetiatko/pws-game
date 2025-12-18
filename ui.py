
import pygame

from settings import FONT_PATH

pygame.init()

font_path = FONT_PATH
money_amount_font = pygame.font.Font(font_path, 30)
watch_time_font = pygame.font.Font(font_path, 50)
powerup_decription = pygame.font.Font(font_path, 50)

class UIElement:
    def __init__(self, scale_size, pos, image_path=None):
        if image_path != None:
            self.image = pygame.transform.scale(
                pygame.image.load(f'{image_path}').convert_alpha(),
                scale_size,
            )

        self.pos = pos
        self.rect = self.image.get_frect(center=self.pos)
        self.display_surface = pygame.display.get_surface()

    def draw(self):
        self.display_surface.blit(self.image, self.pos)


class Button:
    def __init__(
        self,
        pos,
        width,
        height,
        text,
        text_size,
        color,
    ):
        self.pos = pos
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size
        self.color = color

        self.rect = pygame.FRect(pos[0], pos[1], self.width, self.height)
        self.font = pygame.font.Font(font_path, self.text_size)
        
        self.display_surface = pygame.display.get_surface()

    def draw(self):
        pygame.draw.rect(self.display_surface, self.color, self.rect)

        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)

        self.display_surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


class Crosshair(UIElement):
    def __init__(self, offset):
        super().__init__(
            (60, 60),
            pygame.mouse.get_pos(),
            "sprites/crosshair.png",
        )

        self.offset = offset

    def draw(self):
        self.rect.center = pygame.mouse.get_pos() - self.offset
        self.display_surface.blit(self.image, self.rect.topleft + self.offset)


class CoinCounter(UIElement):
    def __init__(self, amount):
        super().__init__(
            (145, 70),
            (20, 200),
            "sprites/coin_counter.png",
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
            (400, 100),
            (5, 20),
            'sprites/healthbar_frame.png',
        )


class ManaBarFrame(UIElement):
    def __init__(self):
        super().__init__(
            (300, 250),
            (2, 17),
            'sprites/manabar_frame.png',
        )


class HealthBar(UIElement):
    def __init__(self):
        super().__init__(
            (220, 20),
            (86, 55),
            'sprites/healthbar.png',
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
            (159, 20),
            (81, 137),
            'sprites/manabar.png',
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
        self.total_seconds = 0

        self.display_surface = pygame.display.get_surface()
        self.pos = (self.display_surface.width / 2.2, 50)

    def draw(self, dt):
        self.time_elapsed += dt
        
        self.minutes = int(self.time_elapsed // 60)
        self.seconds = int(self.time_elapsed % 60)
        self.total_seconds = self.minutes * 60 + self.seconds

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
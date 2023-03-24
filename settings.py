import pygame


class Settings:
    """Class for saving all game settings"""

    def __init__(self, ai_game):
        """Initialize game settings"""

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (59, 186, 186)
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Download background image and get his rect
        self.bg_image = pygame.image.load('images/big_space.bmp')
        self.rect = self.bg_image.get_rect()

        # Create each new bg_image in the center of screen
        self.rect.center = self.screen_rect.center

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (5, 5, 5)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

    def draw_space(self):
        """Draw space in his current position"""
        self.screen.blit(self.bg_image, self.rect)



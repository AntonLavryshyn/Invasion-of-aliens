import pygame


class Settings:
    """Class for saving all game settings"""

    def __init__(self, ai_game):
        """Initialize persistent game settings"""

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
        self.ship_limit = 1

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (5, 5, 5)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # How fast the game should speed up
        self.speedup_scale = 1.1

        # How fast increase alien cost
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialization of variable settings"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction 1 represents the direction to the right; -1 -- to the left
        self.fleet_direction = 1

        # Getting points
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed and cost aliens settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def draw_space(self):
        """Draw space in his current position"""
        self.screen.blit(self.bg_image, self.rect)



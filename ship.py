import pygame


class Ship:
    """Class for ship control"""

    def __init__(self, ai_game):
        """initialize the ship and give it an initial position"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """Download ship image and get it in "react()" """

        self.image = pygame.image.load('images/space_ship2.bmp')
        self.rect = self.image.get_rect()

        """Create a new each ship at the bottom of the screen, in the center"""
        self.rect.midbottom = self.screen_rect.midbottom

        """Save a decimal value for the horizontal position of the ship"""
        self.x = float(self.rect.x)

        """traffic indicator"""
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's current position based on the motion indicator"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        """Update the rect object from self.x"""
        self.rect.x = self.x

    def draw_a_ship(self):
        """draw the ship in its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)



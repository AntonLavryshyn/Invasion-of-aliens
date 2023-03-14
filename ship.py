import pygame


class Ship:
    """Class for ship control"""

    def __init__(self, ai_game):
        """initialize the ship and give it an initial position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        """Download ship image and get it in "react()" """

        self.image = pygame.image.load('images/space_ship.bmp')
        self.rect = self.image.get_rect()

        """Create a new each ship at the bottom of the screen, in the center"""
        self.rect.midbottom = self.screen_rect.midbottom

    def draw_a_ship(self):
        """draw the ship in its current location"""
        self.screen.blit(self.image, self.rect)



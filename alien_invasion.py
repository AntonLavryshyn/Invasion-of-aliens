import sys

import pygame


class AlienInvasion:
    """Generic class that manages game resources and behavior"""

    def __init__(self):
        """Initialize game, create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Alien Invasion")

        """Set the background color"""
        self.bg_color = (215, 22, 55)

    def run_game(self):
        """Start the main game cycle"""
        while True:
            """Monitor mouse and keyboard events"""

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                """Redraw the screen on each iteration"""

                self.screen.fill(self.bg_color)

            """Show the last drawn screen"""
            pygame.display.flip()


if __name__ == '__main__':
    """Create an instance of the game and run the game"""
    ai = AlienInvasion()
    ai.run_game()

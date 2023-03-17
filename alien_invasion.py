import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet


class AlienInvasion:
    """Generic class that manages game resources and behavior"""

    def __init__(self):
        """Initialize game, create game resources"""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main game cycle"""

        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()
            """Monitor mouse and keyboard events"""

    def _check_events(self):
        """Respond to keystrokes and mouse events"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_key_down_events(self, event):
        """react when the key is pressed"""
        if event.key == pygame.K_RIGHT:
            """move the ship to the right"""
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            """move the ship to the left"""
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """react when the key is not pressed"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create new bullet and add it to bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet position and delete old bullets"""
        # Update bullets position
        self.bullets.update()

        # Get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update image on screen and switch to a new screen"""

        self.screen.fill(self.settings.bg_color)
        self.ship.draw_a_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        """Show the last drawn screen"""
        pygame.display.flip()


if __name__ == '__main__':
    """Create an instance of the game and run the game"""
    ai = AlienInvasion()
    ai.run_game()

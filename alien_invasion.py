import sys

import pygame

from time import sleep

from settings import Settings

from game_stats import GameStats

from button import Button

from ship import Ship

from bullet import Bullet

from alien import Alien

from scoreboard import ScoreBoard


class AlienInvasion:
    """Generic class that manages game resources and behavior"""

    def __init__(self):
        """Initialize game, create game resources"""

        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))

        pygame.display.set_caption("Alien Invasion")
        self.settings = Settings(self)
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Create "Play" button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main game cycle"""

        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_bottom(mouse_pos)

    def _check_play_bottom(self, mouse_pos):
        """Start new game when user press button 'Play' """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Cancel game statistics
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()

            # Get rid of excess aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and center it
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

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

    def _ship_hit(self):
        """React to the collision of the alien with the ship"""
        if self.stats.ships_left > 0:
            # Reduce ships_left
            self.stats.ships_left -= 1

            # Get rid of excess aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(2)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_bullets(self):
        """Update bullet position and delete old bullets"""
        # Get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Reaction to the collision of bullets with aliens"""
        # Delete all bullets and aliens with collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)

        self.sb.prep_score()

        # Destroy all bullets and create new fleet
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_aliens(self):
        """
        Check if the fleet is at the edge of the screen
         then update the positions of all aliens
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for bullet collisions with aliens
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look to see if any of the aliens have reached the bottom of the screen
        self._check_aliens_bottom()

    def _create_fleet(self):
        """Create aliens fleet"""
        # Creating aliens and determining the number of aliens in a row
        # Distance between aliens equal to one aliens width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width) + 1

        # Determine how many aliens fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_width -
                            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create a full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x + 75
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number - 100
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """
        Reacts according to whether one of the aliens
        has reached the edge of the screen
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        """Check if any newcomer has reached the bottom edge of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # React as if the ship had been hit
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """Descent of the entire fleet and change of direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update image on screen and switch to a new screen"""

        self.screen.fill(self.settings.bg_color)
        self.ship.draw_a_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw information about score
        self.sb.show_score()

        # Draw button Play if game inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        """Show the last drawn screen"""
        pygame.display.flip()


if __name__ == '__main__':
    """Create an instance of the game and run the game"""
    ai = AlienInvasion()
    ai.run_game()

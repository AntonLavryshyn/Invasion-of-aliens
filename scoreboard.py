import pygame.font


class ScoreBoard:
    """A class that outputs a score"""

    def __init__(self, ai_game):
        """Initialize account-related attributes"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Setting the font for displaying the bill.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare an image with an initial score
        self.prep_score()

    def prep_score(self):
        """Transform score to image"""

        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        # Show the score in the upper right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Show score"""
        self.screen.blit(self.score_image, self.score_rect)

class GameStats:
    """Tracking statistics"""

    def __init__(self, ai_game):
        """Initialization of statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in active mode
        self.game_active = True

    def reset_stats(self):
        """Initialization of statistics that may change during the game"""
        self.ships_left = self.settings.ship_limit
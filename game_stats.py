class GameStats(object):
    """docstring for GameStats."""

    def __init__(self, ai_game):
        """Intialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the game with an inactive flag
        self.game_active = False

    def reset_stats(self):
        """Intitialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit

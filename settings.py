class Settings:
    """A class to store all settins for Alien Invasion."""

    def __init__(self):
        """Initiliaze the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (33, 37, 43)

        # Ship Settings
        self.ship_speed = 1.5

        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (23, 186, 22)

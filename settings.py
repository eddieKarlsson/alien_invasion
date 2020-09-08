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
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (23, 186, 22)
        self.bullets_allowed = 5

        # Alien Settings
        self.alien_speed = 2
        self.fleet_drop_speed = 10
        # Fleet direction 1=right, -1=left
        self.fleet_direction = 1

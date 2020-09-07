import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initiliaze the screen and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settigs = ai_game.settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ships position depending on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settigs.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settigs.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

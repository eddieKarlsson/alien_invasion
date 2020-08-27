import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to manage the Alien"""

    def __init__(self, ai_game):
        """Initiliaze the screen and its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the Alien image and get its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new Alien at the bottom center of the screen
        self.rect.x = self.rect.width
        self.rect.x = self.rect.height

        # Store a decimal value for the Aliens horizontal position
        self.x = float(self.rect.x)

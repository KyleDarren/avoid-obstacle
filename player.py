import pygame
from setting import gravity

class Player(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        # Set the player's attribute
        self.image = pygame.Surface((size, size))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        # The origin of the rectangle is in the center of it
        self.rect.x = position[0] - size/2
        self.rect.y = position[1] - size/2

    def update(self):
        # This condition tells the behavior of the player if the screen is clicked
        left_button, _, _ = pygame.mouse.get_pressed()
        if left_button:
            self.rect.y -= gravity
        else:
            self.rect.y += gravity

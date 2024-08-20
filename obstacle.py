import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        # Set the attributes for obstacles
        self.size = size
        self.image = pygame.Surface((self.size[0], self.size[1]))
        self.image.fill('green')
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update(self):
        # This allow the obstacles to move to the left
        self.rect.x -= 5
        # Removed the obstacles if it is note appearing in the screen
        if self.rect.x < 0 - self.size[0]:
            self.kill()
            print("removed")


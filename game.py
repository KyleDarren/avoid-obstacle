import random
import pygame
from setting import *
from player import Player
from obstacle import Obstacle

class Game:
    def __init__(self, surface):
        self.display_surface = surface
        # Create a player
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player((player_x, player_y), player_size))
        # Create a container for obstacles
        self.obstacles = pygame.sprite.Group()
        # Check if the game is over
        self.isGameOver = False
        print(self.player.sprite.rect.y)

    # This method creates obstacles with random height
    def create_obstacles(self, stop=False):
        height = random.randint(0, screen_height/2)
        width = 50
        x = screen_height
        y = 0
        if self.isGameOver == False:
            # Add obstacles in the container
            self.obstacles.add(Obstacle((x, y), (width, height)))
            self.obstacles.add(Obstacle((x, height+gap_height), (width, screen_height-(gap_height+height))))

    # This method specify what will happen if the player collided in obstacles
    def collision_detection(self):
        collisions = pygame.sprite.groupcollide(self.obstacles, self.player, False, False)
        if collisions:
            print("collided!")
            self.isGameOver = True

    # This method check if the player touches the screen boundary
    def collision_boundary(self):
        if self.player.sprite.rect.y < 0:
            self.isGameOver = True
        elif self.player.sprite.rect.y > screen_height - player_size:
            self.isGameOver = True

    # This method contains different method to be executed while the game is running
    def run(self):
        # This condition tells that the player and obstacles must be updated only if the game is still not over
        if self.isGameOver == False:
            self.player.update()
            self.obstacles.update()
        self.player.draw(self.display_surface)
        self.obstacles.draw(self.display_surface)
        self.collision_detection()
        self.collision_boundary()


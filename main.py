import pygame, sys
from setting import *
from game import Game

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Initialize the game
game = Game(screen)

# Set a timer that trigger a function every 1000 milliseconds
TIMER_EVENT_ID = pygame.USEREVENT + 1
timer_interval = 1000
pygame.time.set_timer(TIMER_EVENT_ID, timer_interval)

# Handle Events
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == TIMER_EVENT_ID:
            # Create obstacles in every iteration
            game.create_obstacles()

    # Set the background color to black
    screen.fill('black')

    # Run the game
    game.run()

    # Update the screen
    pygame.display.update()

    # Set fps to 60
    clock.tick(60)
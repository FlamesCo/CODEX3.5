import pygame, sys 
from pygame.locals import * 
import random 

# Initialize pygame 
pygame.init() 
  
# Set the window size and title 
WINDOW_SIZE = (800, 600) 
screen = pygame.display.set_mode(WINDOW_SIZE) 
pygame.display.set_caption('Mario Game') 
  
# Colors 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
  
# Clock for game loop 
clock = pygame.time.Clock() 
  
# Create the game loop 
while True: 
    # Check for events 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
  
    # Fill the background with white color 
    screen.fill(WHITE) 
  
    # Doom algorithm for the game 
    # Generate random platforms 
    for i in range(10): 
        platform_width = random.randint(50, 100) 
        x = random.randint(0, WINDOW_SIZE[0] - platform_width) 
        y = random.randint(0, WINDOW_SIZE[1] - platform_width) 
        pygame.draw.rect(screen, BLACK, [x, y, platform_width, 5]) 
  
    # Mario's position 
    mario_x = 400
    mario_y = 300
    mario_size = 20
  
    # Draw Mario 
    pygame.draw.ellipse(screen, BLACK, [mario_x, mario_y, mario_size, mario_size]) 
  
    # Update the display 
    pygame.display.update() 
  
    # Set the clock speed 
    clock.tick(60)
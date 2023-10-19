import pygame
# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
# Basic parameters of the screen
WIDTH, HEIGHT = 900, 600
# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf', 20)
font30 = pygame.font.Font('freesansbold.ttf', 30)
font100 = pygame.font.Font('freesansbold.ttf', 100)
# Set the screen to the given paramaters
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Sets the clock 
clock = pygame.time.Clock() 
# Controls the speed of the game. 
FPS = 30

GRAVITY = .05
STOP_BOUNCE = .3





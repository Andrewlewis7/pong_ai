import pygame
from settings import HEIGHT, font20, screen

class Paddle:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.prev_y = posy  # Add a variable to store the previous position of the paddle

        # Rect that is used to control the position and collision of the object
        self.paddleRect = pygame.Rect(posx, posy, width, height)
        # Object that is built on the screen
        self.rect = pygame.draw.rect(screen, self.color, self.paddleRect)

    # Used to display the object on the screen
    def display(self):
        self.rect = pygame.draw.rect(screen, self.color, self.paddleRect)

    def getSection(self, ball):
        # Calculate the relative position of the ball on the paddle
        relative_y = ball.posy - self.posy
        
        # Calculate the height of each section
        section_height = self.height / 3
        
        # Determine which section the ball hits
        if 0 <= relative_y < section_height:
            return "top"
        elif section_height <= relative_y < 2 * section_height:
            return "middle"
        else:
            return "bottom"

    def update(self, yFac):
        # Calculate the speed of the paddle based on the change in position during each update
        y_speed_paddle = self.posy - self.prev_y
        self.prev_y = self.posy

        self.posy = self.posy + self.speed * yFac

        # Restricting the striker to be below the top surface of the screen
        if self.posy <= 0:
            self.posy = 0
        # Restricting the striker to be above the bottom surface of the screen
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height

        # Updating the rect with the new values
        self.paddleRect = (self.posx, self.posy, self.width, self.height)

        return y_speed_paddle

    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)

        screen.blit(text, textRect)

    def getRect(self):
        return self.paddleRect


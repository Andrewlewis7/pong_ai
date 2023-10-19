# ball.py

import pygame
from settings import WIDTH, HEIGHT, screen, GRAVITY, STOP_BOUNCE
import random

class Ball:

    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1
        self.xFac = 1
        self.yFac = -1

    def display(self):
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)

    # The ball ball bounces in different directions based on the section of paddle it hits. 
    def hit(self, section):
        if section == "top":
            self.yFac = -1
            self.xFac *= -1
        elif section == "middle":
            self.xFac *= -1.5
            self.yFac *= 0.1
        elif section == "bottom":
            self.yFac = 1
            self.xFac *= -1
    
    def hit2(self):
        self.xFac *= -1

    def update(self):
        self.posx += self.speed*self.xFac
        self.posy += self.speed*self.yFac

        # If the ball hits the top or bottom surfaces,
        # then the sign of yFac is changed and
        # it results in a reflection
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1

        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0  
            return -1
        else:
            return 0
    #resets the ball in the middle of the screen at a random direction
    def reset(self):
        self.posx = WIDTH//2
        self.posy = HEIGHT//2
        self.xFac = random.choice([-1,1])
        self.yFax = 1
        self.firstTime = 1
        self.speed = 7

    def getRect(self):
        return self.ball


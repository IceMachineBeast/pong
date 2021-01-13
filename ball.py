import pygame, random
from random import *


class Ball:
    def __init__(self, surface, width, height, color=(255, 255, 255)):
        self.color = color
        self.surface = surface
        self.width = width
        self.height = height
        self.speed = 1000

        decider = randint(1, 4)
        if decider == 1:
            self.direction = [self.speed / 2, self.speed / 2]
        elif decider == 2:
            self.direction = [-self.speed / 2, self.speed / 2]
        elif decider == 3:
            self.direction = [-self.speed / 2, -self.speed / 2]
        elif decider == 4:
            self.direction = [self.speed / 2, -self.speed / 2]

        self.posX = 600 - self.width
        self.posY = 400 - self.height
    def drawBall(self, deltaTime):
        self.posX += self.direction[0] * deltaTime
        self.posY += self.direction[1] * deltaTime

        pygame.draw.rect(
            self.surface, self.color, (self.posX, self.posY, self.width, self.height)
        )

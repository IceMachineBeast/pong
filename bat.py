import pygame


class Bat:
    def __init__(self, surface, width, height, color=(255, 255, 255)):
        self.color = color
        self.width = width
        self.height = height
        self.surface = surface

    def drawBat(self, posX, posY):
        pygame.draw.rect(
            self.surface, self.color, (posX, posY, self.width, self.height)
        )

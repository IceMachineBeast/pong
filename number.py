import pygame
import time


class Number:
    def __init__(self, surface, index, size, x, y):
        self.surface = surface
        self.size = size
        self.x = x
        self.y = y
        self.index = index

    def draw(self):
        # Choosing the right number to print

        if self.index == 0:
            self.zero()
        elif self.index == 1:
            self.one()
        elif self.index == 2:
            self.two()
        elif self.index == 3:
            self.three()
        elif self.index == 4:
            self.four()
        elif self.index == 5:
            self.five()
        elif self.index == 6:
            self.six()
        elif self.index == 7:
            self.seven()
        elif self.index == 8:
            self.eight()
        elif self.index == 9:
            self.nine()

    def drawRect(self, x, y):
        pygame.draw.rect(
            self.surface,
            (255, 255, 255),
            (self.x + self.size * x, self.y + self.size * y, self.size, self.size),
        )

    # Here are the function for the numbers
    def zero(self):
        self.drawRect(0, 0)
        self.drawRect(1, 0)
        self.drawRect(2, 0)

        self.drawRect(0, 1)
        self.drawRect(2, 1)

        self.drawRect(0, 2)
        self.drawRect(2, 2)

        self.drawRect(0, 3)
        self.drawRect(2, 3)

        self.drawRect(0, 4)
        self.drawRect(1, 4)
        self.drawRect(2, 4)

    def one(self):
        for x in range(5):
            self.drawRect(2, x)

    def two(self):
        self.drawRect(0, 0)
        self.drawRect(1, 0)
        self.drawRect(2, 0)

        self.drawRect(2, 1)

        self.drawRect(2, 2)
        self.drawRect(1, 2)
        self.drawRect(0, 2)

        self.drawRect(0, 3)

        self.drawRect(0, 4)
        self.drawRect(1, 4)
        self.drawRect(2, 4)

    def three(self):
        self.drawRect(0, 0)
        self.drawRect(1, 0)
        self.drawRect(2, 0)

        self.drawRect(2, 1)

        self.drawRect(0, 2)
        self.drawRect(1, 2)
        self.drawRect(2, 2)

        self.drawRect(2, 3)

        self.drawRect(0, 4)
        self.drawRect(1, 4)
        self.drawRect(2, 4)

    def four(self):
        self.drawRect(0, 0)
        self.drawRect(2, 0)

        self.drawRect(0, 1)
        self.drawRect(2, 1)

        self.drawRect(0, 2)
        self.drawRect(1, 2)
        self.drawRect(2, 2)

        self.drawRect(2, 3)

        self.drawRect(2, 4)

    def five(self):
        self.drawRect(0, 0)
        self.drawRect(1, 0)
        self.drawRect(2, 0)

        self.drawRect(0, 1)

        self.drawRect(2, 2)
        self.drawRect(1, 2)
        self.drawRect(0, 2)

        self.drawRect(2, 3)

        self.drawRect(0, 4)
        self.drawRect(1, 4)
        self.drawRect(2, 4)

    def six(self):
        self.drawRect(0, 0)
        self.drawRect(1, 0)
        self.drawRect(2, 0)

        self.drawRect(0, 1)

        self.drawRect(0, 2)
        self.drawRect(1, 2)
        self.drawRect(2, 2)

        self.drawRect(0, 3)
        self.drawRect(2, 3)

        self.drawRect(0, 4)
        self.drawRect(1, 4)
        self.drawRect(2, 4)

    def seven(self):
        self.drawRect(0, 0)
        self.drawRect(1, 0)
        self.drawRect(2, 0)

        self.drawRect(2, 1)
        self.drawRect(2, 2)
        self.drawRect(2, 3)
        self.drawRect(2, 4)

    def eight(self):
        self.drawRect(0, 0)
        self.drawRect(1, 0)
        self.drawRect(2, 0)

        self.drawRect(0, 1)
        self.drawRect(2, 1)

        self.drawRect(0, 2)
        self.drawRect(1, 2)
        self.drawRect(2, 2)

        self.drawRect(0, 3)
        self.drawRect(2, 3)

        self.drawRect(0, 4)
        self.drawRect(1, 4)
        self.drawRect(2, 4)

    def nine(self):
        self.drawRect(0, 0)
        self.drawRect(1, 0)
        self.drawRect(2, 0)

        self.drawRect(2, 1)
        self.drawRect(0, 1)

        self.drawRect(0, 2)
        self.drawRect(1, 2)
        self.drawRect(2, 2)

        self.drawRect(2, 3)

        self.drawRect(2, 4)


if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((800, 600))

    numbers = Number(surface, 9, 20, 100, 100)
    numbers.draw()
    pygame.display.update()
    time.sleep(2)

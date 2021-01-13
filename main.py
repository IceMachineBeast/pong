#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import bat
import ball
import time
import number


class Game:
    def __init__(self):

        # Game Settings

        self.running = True
        self.size = (1200, 800)
        self.surface = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.victoryLimit = 15
        self.speedBonus = False
        self.currentSpeedBonus = 0

        # Creating the numbers

        self.num0 = number.Number(self.surface, 0, 20, self.size[0] / 2 - 90, 20)
        self.num1 = number.Number(self.surface, 0, 20, self.size[0] / 2 - 160, 20)
        self.num2 = number.Number(self.surface, 0, 20, self.size[0] / 2 + 20, 20)
        self.num3 = number.Number(self.surface, 0, 20, self.size[0] / 2 + 90, 20)

        # Player Settings

        self.player1Points = 0
        self.player2Points = 0
        self.playerSpeed = 1000
        self.playerLength = 120
        self.player1PosY = self.size[1] / 2 - self.playerLength / 2
        self.player2PosY = self.size[1] / 2 - self.playerLength / 2
        self.player1 = bat.Bat(self.surface, 20, self.playerLength)
        self.player2 = bat.Bat(self.surface, 20, self.playerLength)

        # Ball Settings

        self.ballSize = 20
        self.ball = ball.Ball(self.surface, self.ballSize, self.ballSize)

        # Divideing Line Settings (You know that line in the middle)

        self.divLineFreq = 45
        self.divRectHeight = 20
        self.divRectWidth = 10

    def onEvent(self, event):
        # This function is called everytime a pygame event happens

        if event.type == pygame.QUIT:
            self.running = False

    def onRender(self):
        # This function is called every frame to render the object on screen
        self.surface.fill((0, 0, 0))  # Clearing the entire scree

        # Drawing the divideing line with rectangles

        for x in range(0, self.size[0], self.divLineFreq):
            # Creating the line in the middle
            pygame.draw.rect(
                self.surface,
                (255, 255, 255),
                (
                    self.size[0] / 2 - self.divRectWidth,
                    x,
                    self.divRectWidth,
                    self.divRectHeight,
                ),
            )

        # Drawing the bats, numbers  and the ball

        self.player1.drawBat(50, self.player1PosY)
        self.player2.drawBat(self.size[0] - 70, self.player2PosY)
        self.ball.drawBall(self.deltaTime)
        self.num0.draw()
        self.num1.draw()
        self.num2.draw()
        self.num3.draw()

    def onLoop(self):
        # This function is called every frame and takes user input etc.
        if self.player1Points >= self.victoryLimit:
            print("Player1 has won!")
            self.onCleanUp()
        elif self.player2Points >= self.victoryLimit:
            print("Player2 has won!")
            self.onCleanUp()

        keys = pygame.key.get_pressed()  # Getting which keys are currently pressed

        # The first players controls

        if keys[pygame.K_LSHIFT]:
            if self.player1PosY > 0:
                self.player1PosY -= self.playerSpeed * self.deltaTime
        if keys[pygame.K_LCTRL]:
            if self.player1PosY < self.size[1] - self.playerLength:
                self.player1PosY += self.playerSpeed * self.deltaTime

        # The second players controls

        if keys[pygame.K_UP]:
            if self.player2PosY > 0:
                self.player2PosY -= self.playerSpeed * self.deltaTime
        if keys[pygame.K_DOWN]:
            if self.player2PosY < self.size[1] - self.playerLength:
                self.player2PosY += self.playerSpeed * self.deltaTime

        # Checking the horizontal walls for collisions

        if self.ball.posX >= self.size[0] - self.ballSize:
            self.ball.direction[0] *= -1
            print("Player1 gets a point")
            self.player1Points += 1
            del self.ball
            self.ball = ball.Ball(self.surface, self.ballSize, self.ballSize)
            if self.num0.index < 9:
                self.num0.index += 1
            elif self.num0.index >= 9:
                self.num0.index = 0
                self.num1.index += 1

        if self.ball.posX <= 0:
            self.ball.direction[0] *= -1
            print("Player2 gets a point")
            self.player2Points += 1
            del self.ball
            self.ball = ball.Ball(self.surface, self.ballSize, self.ballSize)
            if self.num3.index < 9:
                self.num3.index += 1
            elif self.num3.index >= 9:
                self.num3.index = 0
                self.num2.index += 1

        # Checking the vertical walls for collisions

        if self.ball.posY > self.size[1] - self.ballSize:
            self.ball.direction[1] *= -1
        if self.ball.posY < 0:
            self.ball.direction[1] *= -1

        # Cheking the bats for collisions

        if (
            self.ball.posX <= 70
            and self.ball.posX >= 50
            and self.ball.posY + self.ballSize / 2 >= self.player1PosY
            and self.ball.posY + self.ballSize / 2
            <= self.player1PosY + self.playerLength
        ):
            print("Hit bat1")
            if (
                self.player1PosY
                < self.ball.posY + self.ballSize / 2
                < self.player1PosY + self.playerLength * 0.4
            ):
                self.ball.direction[0] = self.ball.speed / 2
                self.ball.direction[1] = self.ball.speed / 2 * -1
            elif (
                self.player1PosY + self.playerLength
                > self.ball.posY + self.ballSize / 2
                > self.player1PosY + self.playerLength - self.playerLength * 0.4
            ):
                self.ball.direction[0] = self.ball.speed / 2
                self.ball.direction[1] = self.ball.speed / 2
            else:
                self.ball.direction[0] = self.ball.speed
                self.ball.direction[1] = 0
            self.ball.posX += 20
            pygame.mixer.Sound.play(self.pongSound)

        if (
            self.ball.posX >= self.size[0] - 80
            and self.ball.posX <= self.size[0] - 60
            and self.ball.posY + self.ballSize / 2 >= self.player2PosY
            and self.ball.posY + self.ballSize / 2
            < self.player2PosY + self.playerLength
        ):
            print("Hit bat2")
            if (
                self.player2PosY
                < self.ball.posY + self.ballSize / 2
                < self.player2PosY + self.playerLength * 0.4
            ):
                self.ball.direction[0] = self.ball.speed / 2 * -1
                self.ball.direction[1] = self.ball.speed / 2 * -1
            elif (
                self.player2PosY + self.playerLength
                > self.ball.posY + self.ballSize / 2
                > self.player2PosY + self.playerLength - self.playerLength * 0.4
            ):
                self.ball.direction[0] = self.ball.speed / 2 * -1
                self.ball.direction[1] = self.ball.speed / 2
            else:
                self.ball.direction[0] = self.ball.speed * -1
                self.ball.direction[1] = 0
            self.ball.posX -= 20
            pygame.mixer.Sound.play(self.pongSound)

    def onCleanUp(self):
        # Basically closes the program
        pygame.onCleanUp()

    def start(self):
        pygame.init()  # Initiating pygame
        pygame.mixer.init()
        self.pongSound = pygame.mixer.Sound("pong.ogg")  # Loading the pong sound

        currentTime = time.time()  # Needed for time.deltatime
        while self.running:
            previousTime = currentTime
            currentTime = time.time()
            self.deltaTime = currentTime - previousTime
            for event in pygame.event.get():  # Handeling all of the events
                self.onEvent(event)

            # The main game loop

            self.onRender()
            self.onLoop()
            pygame.display.update()
        self.onCleanUp()


## Starting the game ##
game = Game()
game.start()

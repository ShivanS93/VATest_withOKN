# /usr/bin/python3
# Author: Shivan Sivakumaran
# main.py - creates screen that displays the OKN stimulus

import sys
import random
import numpy as np
import pygame
import time

from pygame.locals import *


class DrawCircle:
    def __init__(self, screen_, x_pos, y_pos, radius, diff):
        self.screen_ = screen_
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.diff = diff

    def drawCircle(self):
        white = (255, 255, 255)
        black = (0, 0, 0)
        grey = (128, 128, 128)

        cir_pos = (self.x_pos + self.radius, self.y_pos + self.radius)
        r = self.radius
        d = self.diff

        pygame.draw.circle(self.screen_, white, cir_pos, r, 0)
        pygame.draw.circle(self.screen_, black, cir_pos, r - d, 0)
        pygame.draw.circle(self.screen_, white, cir_pos, r - 3 * d, 0)
        pygame.draw.circle(self.screen_, grey, cir_pos, r - 4 * d, 0)

    def move(self, move_speed):
        self.x_pos = self.x_pos + move_speed
        if self.x_pos < 0:
            self.x_pos = self.screen_.get_size()[0]
        elif self.x_pos > self.screen_.get_size()[0]:
            self.x_pos = 0

    def changeVA(self, acuity):
        """
        changes thickness of circle lines
        """
        self.diff = acuity


def main():
    pygame.init()
    SPEED = 7

    (W, H) = (720, 1280)  # size of windows by pixel
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("OKN_VA")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((128, 128, 128))

    nx, ny = 15, 10  # columns, rows of circles

    a = np.arange(0, W, W / nx)
    b = np.arange(0, H, H / ny)

    circles = [DrawCircle(background, x, y, 50, 5) for x in a for y in b]

    rand_dir = 1
    timer = time.time()

    while True:

        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                sys.exit()

        for circle in circles:
            circle.move(rand_dir * SPEED)  # speed of OKN stimilus
            circle.drawCircle()

        screen.blit(background, (0, 0))
        background.fill((128, 128, 128))
        pygame.display.update()

        if time.time() - timer >= 3:  # length of 'VA' shown for

            pygame.time.delay(500)

            timer = time.time()

            rand_VA = random.randint(0, 10)
            rand_dir = random.choice([-1, 1])

            for circle in circles:
                circle.changeVA(rand_VA)

    return


if __name__ == "__main__":
    main()

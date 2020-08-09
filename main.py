#!python3
# Shivan Sivakumaran
# main.py - runs pygame

import os, sys
import random, math
import pygame

from pygame.locals import *

class squareObject:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

def main():
    # Initiaise screen
    pygame.init()

    infoObj = pygame.display.Info()
    #screen = pygame.display.set_mode((infoObj.current_w, infoObj.current_h))
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption('OKN_VA')

    #get screen dimentions
    width, height = pygame.display.get_surface().get_size()


    #Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((128, 128, 128))

    #create square
    square = pygame.image.load('square.bmp').convert()
    objects = [squareObject(square, random.random()*width, random.random()*height)
               for i in range(50)]



    #Blit everthing on the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #Event loop
    #while 1:
    while True:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                sys.exit()
 
        screen.blit(background, (0,0))

        for o in objects:
            if o.x <= 0:
                o.x = width
                o.y = random.random() * height
            o.x = o.x - 17
            screen.blit(o.image, (o.x, o.y))

        pygame.display.flip()

if __name__ == '__main__': main()

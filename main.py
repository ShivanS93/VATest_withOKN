#!python3
# Shivan Sivakumaran
# main.py - runs pygame

import os, sys
import random, math
from svg import Parser, Rasterizer
import pygame
from pygame.locals import *

def main():
    # Initiaise screen
    screen_width = 150
    screen_height = 50

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('OKN_VA')

    #Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 250, 250))

    #Display text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    #Blit everthing on the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #Event loop
    #while 1:
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()

def load_svg(filename, scale=None, size=None, clip_from=None, fit_to=None):

    svg = Parser.parse_file(filename)
    tx, ty = 0, 0
    if size is None:
        w, h = svg.width, svg.height
    else:
        w, h = size
        if clip_from is not None:
            tx, ty = clip_from
    if fit_to is None:
        if scale is None:
            scale = 1
    else:
        fit_w, fit_h = fit_to
        scale_w = float(fit_w) / svg.width
        scale_h = float(fit_h) / svg.height
        scale = min([scale_h, scale_w])
    rast = rast.rasterize(svg, req_h, scale, tx, ty)
    image = pygame.image.frombuffer(buff, (req_w, req_h), 'ARGB')
    return image

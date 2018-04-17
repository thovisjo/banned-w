#!/usr/bin/python

import pygame, random, sys, os, loggin
assert sys.version_info >= 3.4, 'This script requires at least Python 3.4'

green = (0,255,0)

class Player(pygame.sprite.Sprite):
    def __init__(self,position,direction,lives,size,orientation):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.iamge.load(str(img)).conver()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(green)
        (self.rect.x, self.rect.y) = position
        self.direction = direction
        self.orientation = orientation

    def move_forward():
        self.direction[0] = math.sin(-math.radians(self.orientation))
        self.direction[1] = math.cos(math.radians(self.orientation))

        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]
        
    

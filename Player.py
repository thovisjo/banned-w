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

    def move_forward(amount):
        
        self.direction[1] = math.cos(math.radians(self.orientation))

        
        self.position[1] += self.direction[1]*amount

    def strafe(self,amount):
        self.direction[0] = math.sin(-math.radians(self.orientation))
        self.position[0] += self.direction[0]*amount

    def rotate(self,amount):
        self.orientation += amount

        if self.orientation == 361:
            self.orientation = 0

        if self.orientation == -1:
            self.orientation = 360

        rotation = pygame.transform.rotate(self.image,amount)
        rotation_rect = rotation.get_rect(center = rect.center)
        return rotation,rotation_rect

    def fire(self):
        firing_angle = [0,0]
        firing_angle[0] = math.sin(-math.radians(self.orientation)) * self.image.get_width()
        firing_angle[1] = math.cos(-math.radians(self.orientation)) * self.image.get_width

        new_bullet = Bullet((self.position[0]+firing_angle[0], self.position[1]+firing_angle[1]/2), self.orientation)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, angle, speed = 10):
        

        

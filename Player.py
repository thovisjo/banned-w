#!/usr/bin/python

import pygame, random, sys, os, logging, math

black = (0,0,0)
green = (0,255,0)

class Player(pygame.sprite.Sprite):
    def __init__(self,position,direction,lives,size,rotation):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Wresize.png').convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black)
        (self.rect.x, self.rect.y) = position
        self.direction = direction
        self.lives = lives
        self.position = position
        self.rotation = 0

    def move(self, xPlus = 0, yPlus = 0):

        
        if self.rect.x > 3 and xPlus < 0: 
            self.rect.x += xPlus
        if self.rect.x < 770 and xPlus > 0:
            self.rect.x += xPlus
        if self.rect.y > 78 and yPlus <0:
            self.rect.y += yPlus
        if self.rect.y < 575 and yPlus > 0:
            self.rect.y += yPlus

        position = (self.rect.y, self.rect.x)

    def rotate(self, key):
        temp_loc = self.position
        if key == "up":
            if self.rotation == 0:
                pass
            elif self.rotation == 1:
                self.image = pygame.transform.rotate(self.image,270)
                self.rotation = 0
            elif self.rotation == 2:
                self.image = pygame.transform.rotate(self.image,180)
                self.rotation = 0
            elif self.rotation == 3:
                self.image = pygame.transform.rotate(self.image,90)
                self.rotation = 0
        if key =='down':
            if self.rotation == 2:
                pass
            elif self.rotation == 3:
                self.image = pygame.transform.rotate(self.image,270)
                self.rotation = 2
            elif self.rotation == 0:
                self.image = pygame.transform.rotate(self.image,180)
                self.rotation = 2
            elif self.rotation == 1:
                self.image = pygame.transform.rotate(self.image,90)
                self.rotation = 2
        if key == 'left':
            if self.rotation == 1:
                pass
            elif self.rotation == 2:
                self.image = pygame.transform.rotate(self.image,270)
                self.rotation = 1
            elif self.rotation == 3:
                self.image = pygame.transform.rotate(self.image,180)
                self.rotation = 1
            elif self.rotation == 0:
                self.image = pygame.transform.rotate(self.image,90)
                self.rotation = 1

        if key == 'right':
            if self.rotation == 3:
                pass
            elif self.rotation == 0:
                self.image = pygame.transform.rotate(self.image,270)
                self.rotation = 3
            elif self.rotation == 1:
                self.image = pygame.transform.rotate(self.image,180)
                self.rotation = 3
            elif self.rotation == 2:
                self.image = pygame.transform.rotate(self.image,90)
                self.rotation = 3

        self.position = temp_loc
        print(self.position)
            
                
                


    def fire(self):
        
        new_bullet = Bullet((self.position[0],self.position[1], rotation))

    def update(self):
        """
        """
class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, angle, speed = 10):
        
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(str('bullet.png')).convert()
       self.rect = self.image.get_rect()
       (self.rect.x, self.rect.y) = position
       self.angle = angle
       self.speed = speed
    def getPosition(self):
       return self.position

        

        

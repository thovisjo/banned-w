
import pygame, random, sys, os, logging

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

class Enemy(pygame.sprite.Sprite):
    def __init__(self,position,letter):
        pygame.sprite.Sprite.__init__(self)
        self.origPosition = position
        self.image = pygame.image.load(os.path.join('.', 'enemy.png')).convert()
        self.rect = self.image.get_rect()
        (self.rect.x, self.rect.y) = (0, 0)
        self.ramp_up = 1
        self.max_dx = 5
        self.alive = 1
        self.position = position
        

    def get_position(self):
        return (self.rect.x, self.rect.y)

    def move(self, direction):
        self.rect.x += direction[0]
        self.rect.y += direction[1]
        self.position = (self.rect.x,self.rect.y)

    def reset(self):
        (self.rect.x, self.rect.y) = self.origPosition

    def locatePlayer(self,playerLocation):
        if self.alive:
            if playerLocation[0] > self.rect.x & playerLocation[1] > self.rect.y:
                self.move((5,5))
            elif playerLocation[0] < self.rect.x & playerLocation[1] < self.rect.y:
                self.move((-5,-5))
            elif playerLocation[0] > self.rect.x & playerLocation[1] < self.rect.y:
                self.move((5,-5))
            elif playerLocation[0] < self.rect.x & playerLocation[1] > self.rect.y:
                self.move((5, -5))
            elif playerLocation[0] == self.rect.x & playerLocation[1] > self.rect.y:
                self.move((0,5))
            elif playerLocation[0] == self.rect.x & playerLocation[1] < self.rect.y:
                self.move((0, -5))
            elif playerLocation[0] > self.rect.x & playerLocation[1] == self.rect.y:
                self.move((5, 0))
            elif playerLocation[0] < self.rect.x & playerLocation[1] == self.rect.y:
                self.move((-5,0))
            else:
                self.move((0,0))

    def update(self,playerLocation,bullets):
        self.locatePlayer(playerLocation)
        for b in bullets:
            if pygame.sprite.collide_rect(b, self):
                self.alive = 0
                self.location = (1000,1000)
                



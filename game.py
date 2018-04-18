#!/usr/bin/python

from pygame import *
import pygame, random, sys, os, logging, math
from Enemy import Enemy
from player import Player, Bullet
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

logging.basicConfig(format = ' [%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

screen_size = (800,600)
FPS = 60
lives = 5

black = (0,0,0)
white = (255,255,255)
gray = (152,152,152)

def fire(player_obj):
        
    new_bullet = Bullet((player_obj.rect.center), player_obj.rotation)
    return new_bullet

def new_enemy():
    new_enemy = Enemy((random.randint(1,780),random.randint(80,580)),'w')
    return new_enemy

def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    enemy_count = 2
    kills = 0
    enemies = pygame.sprite.Group()
    players = pygame.sprite.Group()
    player = Player([200,200],[0,0],3,(20,20), 0)
    first_enemy = Enemy((random.randint(1,780),random.randint(80,580)),'w')
    enemies.add(new_enemy)
    bullets = pygame.sprite.Group()
    players.add(player)
    mixer.init()
    mixer.music.load('425255__eardeer__howtowintheloundnesswars.ogg')
    mixer.music.play()
    
    while True:
        clock.tick(FPS)
        screen.fill(gray)
        pygame.draw.lines(screen, black, False, [(0,75),(800,75)])

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            player.move(yPlus = 1)

        if keys[pygame.K_w]:
            player.move(yPlus = -1)
            
        if keys[pygame.K_d]:
            player.move(xPlus = 1)

        if keys[pygame.K_a]:
            player.move(xPlus = -1)

        if keys[pygame.K_UP]:
            player.rotate('up')

        if keys[pygame.K_DOWN]:
            player.rotate('down')

        if keys[pygame.K_LEFT]:
            player.rotate('left')

        if keys[pygame.K_RIGHT]:
            player.rotate("right")

        if keys[pygame.K_SPACE]:
            bullets.add(fire(player))

        players.update()
        bullets.update()
        enemies.update()
        enemies.draw(screen)
        players.draw(screen)
        bullets.draw(screen)
        pygame.display.flip()
        

        
        
if __name__ == '__main__':
    main()

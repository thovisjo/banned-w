#!/usr/bin/python


import pygame, random, sys, os, logging, math
from player import Player, Bullet
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

logging.basicConfig(format = ' [%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

screen_size = (800,600)
FPS = 60
gravity = 2
friction = .03
lives = 5

black = (0,0,0)
white = (255,255,255)
gray = (152,152,152)

def rotate_sprite(image, rect, angle):
        rotate_image = pygame.transform.rotate(image, angle)
        rotate_rect = rotate_image.get_rect(center=rect.center)
        return rotate_image,rotate_rect

def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    enemy_count = 3
    kills = 0
    enemies = []
    bullets = []
    players = pygame.sprite.Group()
    player = Player([200,200],[0,0],3,(20,20), 0)
    players.add(player)
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
            player.fire()

        players.update()

        players.draw(screen)

        pygame.display.flip()
        

        
        
if __name__ == '__main__':
    main()

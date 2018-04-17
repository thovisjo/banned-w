#!/usr/bin/python


import pygame, random, sys, os, logging, math, Player
assert sys.version_info >= 3.4, 'This script requires at least Python 3.4'

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

    while True:
        clock.tick(FPS)
        screen.fill(gray)
        pygame.draw.lines(screen, black, False, [(0,75),(800,75)])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        if keys[pygame.K_w]:
            player.move_forward(1)

        if keys[pygame.K_s]:
            player.move_forward(-1)

        if keys[pygame.K_d]:
            player.strafe(1)

        if keys[pygame.K_a]:
            player.strafe(-1)

        if keys[pygame.K_e]:
            player.rotate(1)

        if keys[pygame.K_q]:
            player.rotate(-1)

        if keys[pygame.K_SPACE]:
            player.fire()

        enemies.update()
        bullets.update()
        players.update()

        enemies.draw(screen)
        players.draw(screen)
        bullets.draw(screen)

        
        
if __name__ == '__main__':
    main()

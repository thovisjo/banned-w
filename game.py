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
lives = 3

black = (0,0,0)
white = (255,255,255)
gray = (152,152,152)


def fire(player_obj):
        
    new_bullet = Bullet((player_obj.rect.center), player_obj.rotation)
    return new_bullet

def new_enemy(player_obj):
    new_enemy = Enemy(player_space_enemy_roller(player_obj))
    return new_enemy

def player_space_enemy_roller(player_obj):
    spawnpoint = (random.randint(1,780),random.randint(80,580))
    if player_obj.position[0] + 500 < spawnpoint[0] < player_obj.position[0] - 500 and player_obj.position[1] + 500 < spawnpoint[1] < player_obj.position[1] - 50:
        spawnpoint = player_space_enemy_roller(player_obj)
    return spawnpoint
        

def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    enemy_count = 2
    kills = 0
    times_added = 0
    enemies = pygame.sprite.Group()
    players = pygame.sprite.Group()
    player = Player([400,250],[0,0],3,(20,20), 0)
    enemies.add(new_enemy(player))
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
            player.move(yPlus = 2)

        if keys[pygame.K_w]:
            player.move(yPlus = -2)
            
        if keys[pygame.K_d]:
            player.move(xPlus = 2)

        if keys[pygame.K_a]:
            player.move(xPlus = -2)

        if keys[pygame.K_UP]:
            player.rotate('up')
            bullets.add(fire(player))

        if keys[pygame.K_DOWN]:
            player.rotate('down')
            bullets.add(fire(player))

        if keys[pygame.K_LEFT]:
            player.rotate('left')
            bullets.add(fire(player))

        if keys[pygame.K_RIGHT]:
            player.rotate("right")
            bullets.add(fire(player))
            

        if player.lives <= 0:
            pygame.quit()
            sys.exit(0)

        if player.lives > 0:
            pygame.draw.rect(screen, (255,0,0), (150, 20, 15, 15))

        if player.lives > 1:
            pygame.draw.rect(screen, (255,0,0), (175, 20, 15, 15))

        if player.lives > 2:
            pygame.draw.rect(screen, (255,0,0), (200, 20, 15, 15))



        if times_added*2000 < pygame.time.get_ticks():
            times_added +=1
            for i in range(0,times_added):
                new_nme = new_enemy(player)
                enemies.add(new_nme)


        players.update(enemies)
        bullets.update(enemies)
        enemies.update(player.position, players, bullets)
        enemies.draw(screen)
        players.draw(screen)
        bullets.draw(screen)
        pygame.display.flip()
        

        
        
if __name__ == '__main__':
    main()

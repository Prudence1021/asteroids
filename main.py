# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from asteroid import *
from shot import *

def main():

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for i in updatable:
            i.update(dt)
        for q in asteroids:
            if q.collision(player):
                exit("Game over!")
        for n in drawable:
            n.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000












if __name__ == "__main__":
    main()
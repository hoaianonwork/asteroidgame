import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, drawable, updatable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit(1)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid shot")
                    asteroid.split()
                    shot.kill()
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()

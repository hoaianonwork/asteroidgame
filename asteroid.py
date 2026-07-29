from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand = random.uniform(20, 50)
            newasr1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            newasr2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            newasr1.velocity = self.velocity.rotate(rand)*1.2
            newasr2.velocity = self.velocity.rotate(rand+180)*1.2
            
                        

""" FUTURE UPDATE
- Add a scoring system
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped
"""
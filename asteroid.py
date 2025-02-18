import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        # destroy object and exit of too small
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # create new angle and smaller radius
        randomAngle = random.uniform(20, 50)
        newRadius = self.radius - ASTEROID_MIN_RADIUS

        # create first new asteroid
        newDir_A = self.velocity.rotate(randomAngle)
        asteroid = Asteroid(self.position.x, self.position.y, newRadius)
        asteroid.velocity = newDir_A * 1.2

        # create second new asteroid
        newDir_B = self.velocity.rotate(-randomAngle)
        asteroid = Asteroid(self.position.x, self.position.y, newRadius)
        asteroid.velocity = newDir_B * 1.2

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    
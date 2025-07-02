from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        velocity_a = self.velocity.rotate(split_angle)
        velocity_b = self.velocity.rotate(-split_angle)
        asteroid_a = Asteroid(self.position.x, 
                              self.position.y, 
                              self.radius-ASTEROID_MIN_RADIUS)
        asteroid_b = Asteroid(self.position.x, 
                              self.position.y, 
                              self.radius-ASTEROID_MIN_RADIUS)
        asteroid_a.velocity = velocity_a
        asteroid_b.velocity = velocity_b
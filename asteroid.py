import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        new_velocity = self.velocity.rotate(split_angle)
        new_velocity_inv = self.velocity.rotate(split_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        for i in range(0, 2):
            asteroid = asteroid = Asteroid(
            self.position[0],
            self.position[1],
            new_radius)
            if i == 0:
                asteroid.velocity = new_velocity * 1.2
            else:
                asteroid.velocity = new_velocity_inv * 1.2 
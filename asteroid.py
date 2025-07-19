import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,Screen):
        pygame.draw.circle(Screen, (255,200,0), self.position, self.radius)
        return
    def update(self,dt):
        self.position += self.velocity * dt
        return
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        random_angle = random.randint(20,50)

        first_new_asteroid = Asteroid(self.position[0],self.position[1],self.radius- ASTEROID_MIN_RADIUS)
        first_new_asteroid.velocity = self.velocity.rotate(random_angle) * ASTEROID_ACC_ON_SPLIT
        
        second_new_asteroid = Asteroid(self.position[0],self.position[1],self.radius- ASTEROID_MIN_RADIUS)
        second_new_asteroid.velocity = self.velocity.rotate(-random_angle) * ASTEROID_ACC_ON_SPLIT
        self.kill()
        return

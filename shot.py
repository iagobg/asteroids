import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self,Screen):
        pygame.draw.circle(Screen, (255,0,0), self.position, self.radius)
        return
    def update(self,dt):
        self.position += self.velocity * dt
        return
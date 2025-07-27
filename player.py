import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):


    def __init__(self,x,y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,Screen):
        pygame.draw.polygon(Screen, (255,255,255), self.triangle(),2)
        return

    def update(self, dt):
        self.timer -= dt
        self.position += self.velocity * dt
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        # if keys[pygame.K_a]:
        #     self.rotate(-dt)
        # if keys[pygame.K_d]:
        #     self.rotate(dt)

        if keys[pygame.K_SPACE] or mouse[0]:
            self.shoot()
        move_direction = pygame.Vector2(0, 0)
        if keys[pygame.K_w]:
            move_direction += pygame.Vector2(0, 1)
        if keys[pygame.K_s]:
            move_direction += pygame.Vector2(0, -1)
        if keys[pygame.K_a]:
            move_direction += pygame.Vector2(1, 0)
        if keys[pygame.K_d]:
            move_direction += pygame.Vector2(-1, 0)
        
        mouse_pos = pygame.mouse.get_pos()
        direction = pygame.Vector2(mouse_pos) - self.position
        if direction.length_squared() > 0:
            self.rotation = pygame.Vector2(0, 1).angle_to(direction)

        if move_direction.length_squared() > 0:
            move_direction =move_direction.normalize()
            move_direction = move_direction.rotate(self.rotation)
            self.velocity += move_direction * dt * PLAYER_ACCELERATION

        return

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return

    def accelerate(self, dt, sideways=False):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if sideways:
            forward = forward.rotate(90)
        self.velocity += forward* dt *PLAYER_ACCELERATION
        return
    
    def shoot(self):
        if self.timer > 0:
            return
        shot = Shot(self.position[0],self.position[1], SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
        return


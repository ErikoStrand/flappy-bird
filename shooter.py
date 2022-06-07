import pygame
class Shooter:
    position = pygame.Vector2()
    width = 25
    height = 25
    direction = 0
    hasBullet = True
    def __init__(self):
        self.position.xy = 50, 400
        self.gravity = 125
        self.acceleration = pygame.math.Vector2(0, self.gravity)
        self.velocity = pygame.math.Vector2(0, 0)
        self.jumping = False
    def update(self, dt):
        self.jump(dt)
        if self.jumping:
            self.velocity.y *= .5
            self.jumping = False
    def jump(self, dt):
        if self.position.y < 600:
            self.velocity.y += self.acceleration.y * dt * 5
            if self.velocity.y > 250: self.velocity.y = 250
            if self.velocity.y < -400: self.velocity.y = -400
            self.position.y += self.velocity.y * (dt * 2) + (self.position.y * 0.5) * (dt * dt)
        if self.position.y > 600:
            self.position.y = 600 - self.width
            self.velocity.y = 0
        
    def reset(self):
        self.position.y = 400
        self.velocity.y = -200
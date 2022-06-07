import pygame
class Shooter:
    position = pygame.Vector2()
    width = 25
    height = 25
    direction = 0
    hasBullet = True
    def __init__(self):
        self.position.xy = 50, 400
    def setDirection(self, direction):
        self.direction = direction
    def update(self, dt):
        self.direction = 0
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_SPACE]:
            self.direction = 1
        if not keys[pygame.K_SPACE]:
            self.direction = -1
        if (not(self.position.y < 0 and self.direction == 1) and not(self.position.y + self.width > 600 and self.direction == -1)):
            self.position.xy = (self.position.x, self.position.y - self.direction*320*dt) 
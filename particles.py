import pygame
class particles:
    def __init__(self, display, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.display = display
        
    def update(self, dt):
        self.x -= 60*dt
        self.y += 60*dt
        self.size -= 60*dt
        
    def draw(self):
        pygame.draw.rect(self.display, (120, 120, 120), (self.x, self.y, self.size, self.size))
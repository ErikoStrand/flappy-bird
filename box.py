import pygame
class Box:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.heigth)
    def update(self, dt):
        self.x = (self.x - 5*60*dt)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.heigth)
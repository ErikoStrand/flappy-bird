import pygame, sys
from shooter import Shooter
from box import Box
import numpy as np
pygame.init()
pygame.font.init()

(width, heigth) = (400, 600)
display = pygame.display.set_mode((width, heigth))

background = (255, 255, 255)
bird = (150, 150, 150)
clock = pygame.time.Clock()
boxes = []
shooter = Shooter()
NEW_PILLAR = pygame.USEREVENT
pygame.time.set_timer(NEW_PILLAR, 1000)
Test = Box(400, 250, 50, 350)
while 1:
    dt = clock.tick(120) / 1000
    player = pygame.Rect(shooter.position.x, shooter.position.y, shooter.width, shooter.height)
    shooter.setDirection(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == NEW_PILLAR:
            x = 400
            y = np.random.randint(250, 350)
            width = 50
            height = np.random.randint(350, 600)
            boxes.append(Box(x, y, width, height))
    #update
    Test.update(dt)
    shooter.update(dt)
           
    #draw 
    display.fill(background) 
    pygame.draw.rect(display, bird, player)
    
    pygame.draw.rect(display, (100, 100, 100), Test.rect)       
    pygame.display.flip()
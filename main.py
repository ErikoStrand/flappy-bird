import pygame, sys
from shooter import Shooter
from box import Box
import numpy as np
pygame.init()
pygame.font.init()

(width, heigth) = (400, 600)
display = pygame.display.set_mode((width, heigth))
middle_font = pygame.font.Font("Pokemon GB.ttf", 80)
background = (255, 255, 255)
bird = (150, 150, 150)
clock = pygame.time.Clock()
boxes = []
shooter = Shooter()
NEW_PILLAR = pygame.USEREVENT
pygame.time.set_timer(NEW_PILLAR, 1000)
Test = Box(400, 250, 50, 350)
running = False
main_menu = True
score = 0
def reset():
    global boxes
    boxes = []
    
while main_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            main_menu = False
            running = True
            
    display.fill(background)
    shooter.reset()
    reset()          
    pygame.display.flip()
    while running:
        dt = clock.tick(120) / 1000
        player = pygame.Rect(shooter.position.x, shooter.position.y, shooter.width, shooter.height)
        hit_score = pygame.Rect(shooter.position.x, shooter.position.y, 1, shooter.height)
        shooter.setDirection(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == NEW_PILLAR:
                x = 400
                y = np.random.randint(350, 500)
                width = 50
                height = 600 - y
                xtop = 400
                ytop = 0
                widthtop = 50
                heigthtop = y - 100
                boxes.append(Box(xtop, ytop, widthtop, heigthtop))
                boxes.append(Box(x, y, width, height))
                
        #update
        for box in boxes:
            box.update(dt)
            if box.x < -50:
                boxes.remove(box)
                score += 0.5
    
                
        shooter.update(dt)
        
        for box in boxes:    
            if player.colliderect(box):  
                running = False
                main_menu = True    
        #draw 
        display.fill(background) 
        a, b = pygame.font.Font.size(middle_font, str(score))
        draw = middle_font.render(str(score), False, (150, 150, 150))
        display.blit(draw, (200 - a/2, 300))
        pygame.draw.rect(display, bird, player)
        
        for box in boxes:
            pygame.draw.rect(display, (100, 100, 100), box.rect)       
        pygame.display.flip()
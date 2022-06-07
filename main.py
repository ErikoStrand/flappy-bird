import pygame, sys
from shooter import Shooter
from box import Box
import numpy as np
pygame.init()
pygame.font.init()

(width, heigth) = (400, 600)
display = pygame.display.set_mode((width, heigth))
middle_font = pygame.font.Font("PokemonGB.ttf", 80)
home_font = pygame.font.Font("PokemonGB.ttf", 20)
background = (255, 255, 255)
deactive = (200, 200, 200)
active = (150, 150, 150)
bird = (150, 150, 150)
start_button = pygame.Rect(125, 200, 150, 50)
clock = pygame.time.Clock()
boxes = []
shooter = Shooter()
NEW_PILLAR = pygame.USEREVENT
pygame.time.set_timer(NEW_PILLAR, 750)
Test = Box(400, 250, 50, 350)
running = False
main_menu = True
score = 0
jump = True
def reset():
    global boxes, score
    boxes = []
    score = 0
while main_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                pygame.draw.rect(display, active, start_button)
                pygame.display.flip()
                pygame.time.wait(200)
                main_menu = False
                running = True
            
    display.fill(background)
    a, b = pygame.font.Font.size(home_font, "Flopping Bird")
    draw = home_font.render("Flopping Bird", False, (150, 150, 150))
    display.blit(draw, (200 - a/2, 100))
    pygame.draw.rect(display, deactive, start_button)
    reset()          
    pygame.display.flip()
    while running:
        dt = clock.tick(120) / 1000
        player = pygame.Rect(shooter.position.x, shooter.position.y, shooter.width, shooter.height)
        hit_score = pygame.Rect(shooter.position.x, 0, 1, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == NEW_PILLAR:
                x = 400
                y = np.random.randint(200, 500)
                width = 50
                height = 600 - y
                xtop = 400
                ytop = 0
                widthtop = 50
                heigthtop = y - 150
                boxes.append(Box(xtop, ytop, widthtop, heigthtop))
                boxes.append(Box(x, y, width, height))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and jump:
                    jump = False
                    shooter.jumping = True
                    shooter.velocity.y -= 15000
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jump = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and jump:
                    jump = False
                    shooter.jumping = True
                    shooter.velocity.y -= 15000
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    jump = True
        #update
        for box in boxes:
            box.update(dt)
            if box.x < -50:
                boxes.remove(box)
        
        shooter.update(dt)
        
        for box in boxes:
            if hit_score.colliderect(box):
                score += 1/38    
            if player.colliderect(box):  
                running = False
                main_menu = True    
        #draw 
        display.fill(background) 
        a, b = pygame.font.Font.size(middle_font, str(int(score)))
        draw = middle_font.render(str(int(score)), False, (150, 150, 150))
        display.blit(draw, (200 - a/2, 300))
        
        pygame.draw.rect(display, bird, player)
        
        for box in boxes:
            pygame.draw.rect(display, (100, 100, 100), box.rect)       
        pygame.display.flip()
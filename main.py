from turtle import back
import pygame, sys
import pickle
from shooter import Shooter
from box import Box
import numpy as np
from button import button
from particles import particles
pygame.init()
pygame.font.init()

(width, heigth) = (400, 600)
display = pygame.display.set_mode((width, heigth))
middle_font = pygame.font.Font("PokemonGB.ttf", 80)
home_font = pygame.font.Font("PokemonGB.ttf", 15)
background = (255, 255, 255)
deactive = (200, 200, 200)
active = (150, 150, 150)
bird = (150, 150, 150)
text_color = (150, 150, 150)
start_button = pygame.Rect(125, 200, 150, 50)
clock = pygame.time.Clock()
boxes = []
particles_list = []
shooter = Shooter(50, 400)
NEW_PILLAR = pygame.USEREVENT
PLAY_TIME = pygame.USEREVENT + 1
SAVE_TIMER = pygame.USEREVENT + 2
pygame.time.set_timer(SAVE_TIMER, 2500)
pygame.time.set_timer(PLAY_TIME, 1000)
pygame.time.set_timer(NEW_PILLAR, 750)
Test = Box(400, 250, 50, 350)
running = False
main_menu = True
stats_show = False
score = 0
jump = True
#stats = {0: ["Jumps: ", 0, ""], 1: ["deaths: ", 0, ""], 2: ["high_score: ", 0, ""], 3: ["pillars_passed: ", 0, ""], 4: ["time: ", 0, "s"]} 
#with open("stats.dat", "wb") as f:
    #pickle.dump(stats, f) 
with open("stats.dat", "rb") as f:
    stats = pickle.load(f)
    print(stats)

def reset():
    global boxes, score
    for box in boxes:
        boxes.remove(box)  
    boxes = []
    score = 0
def draw_stats():
    for i in range(len(list(stats))): 
        a, b = pygame.font.Font.size(home_font, str(stats[i][0]) + str(int(stats[i][1])) + str(stats[i][2]))
        draw = home_font.render(str(stats[i][0] + str(int(stats[i][1])) + str(stats[i][2])), False, (150, 150, 150))
        display.blit(draw, (200 - a/2, 50 * i + 50))   
        
stats_button = button("Stats", 30, 125, 275, 150, 50, deactive)
start_button2 = button("Start", 30, 125, 200, 150, 50, deactive)
game_name = button("Floppy Bird", 50, 50, 50, 300, 50, background)
back_button = button("Back", 20, 10, 10, 50, 25, deactive)
while main_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                pygame.draw.rect(display, active, start_button)
                pygame.display.flip()
                pygame.time.wait(200)
                #print(stats)
                main_menu = False
                running = True
        if stats_button.update(event, display, active):
            main_menu = False
            stats_show = True
            
    display.fill(background)
    game_name.draw_button(display, text_color)
    start_button2.draw_button(display, text_color)
    stats_button.draw_button(display, text_color)
    reset()          
    pygame.display.flip()
    while stats_show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if back_button.update(event, display, active):
            main_menu = True
            stats_show = False
                    
        display.fill(background)
        back_button.draw_button(display, text_color)
        draw_stats()     
           
        pygame.display.flip()
        
        
        
        
    while running:
        if score > stats[2][1]:
            stats[2][1] = score
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
                
            if event.type == PLAY_TIME:
                stats[4][1] += 1
            if event.type == SAVE_TIMER:
                print("Saved")
                with open("stats.dat", "wb") as f:
                    pickle.dump(stats, f)
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and jump:
                    jump = False
                    shooter.jumping = True
                    shooter.velocity.y -= 15000
                    stats[0][1] += 1
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jump = True
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and jump:
                    particles_list.append(particles(display, shooter.position.x, shooter.position.y + 10, 25))
                    jump = False
                    shooter.jumping = True
                    shooter.velocity.y -= 15000
                    stats[0][1] += 1
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    jump = True
        #update
        for box in boxes:
            box.update(dt)
            if box.x < -50:
                boxes.remove(box)
        
        shooter.update(dt)
        if shooter.position.y < 0:
            shooter.position.y = 0
            shooter.velocity.y = 0
        if shooter.position.y >= 575:
            shooter.position.y = 575
            shooter.velocity.y = 0
        for particle in particles_list:
            particle.update(dt)
            if particle.x < -50:
                particles_list.remove(particle)
        for box in boxes:
            if hit_score.colliderect(box):
                score += 1/38
                stats[3][1] += 1/38
            if player.colliderect(box):
                stats[1][1] += 1
                running = False
                main_menu = True    
        #draw 
        display.fill(background) 
        a, b = pygame.font.Font.size(middle_font, str(int(score)))
        draw = middle_font.render(str(int(score)), False, (150, 150, 150))
        display.blit(draw, (200 - a/2, 300))
        
        pygame.draw.rect(display, bird, player)
        
        for particle in particles_list:
            particle.draw()
        for box in boxes:
            pygame.draw.rect(display, (100, 100, 100), box.rect)       
        pygame.display.flip()
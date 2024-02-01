import pygame
from pygame.locals import *
from sys import exit
import random




pygame.init()

width = 650
height = 650
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True



def player1( pos_y = 0):
    player_pos = (10 , pos_y,20,80)
    player_1 = pygame.draw.rect(screen, (255,255,255),player_pos, 40)
    return player_1

player_1_position_y = 0



def ball(x,y):
    ball_pos = (x,y)
    ball = pygame.draw.circle(screen, (255,255,255), ball_pos, 10)
    return ball

x = 0
y = 0

direction = True

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    if pygame.key.get_pressed()[K_w]:
        player_1_position_y = player_1_position_y + 10
        
    if pygame.key.get_pressed()[K_s]:
        player_1_position_y = player_1_position_y - 10
        
    screen.fill("black")
    player = player1(player_1_position_y)

    
    if direction == True:
        x += 1
        y += 1
    else:
        x -= 1
        y -= 1
        
    
    ball_ = ball(x,y)
    
    if ball_.colliderect(player):
        direction = False
            
        
        
        x = player_1_position_y
        print("colidiu") 
 
 
    pygame.display.flip()

    dt = clock.tick(60)

pygame.quit()

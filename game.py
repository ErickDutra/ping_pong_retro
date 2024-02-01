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


def quadra_superior(): 
    limite = pygame.draw.line(screen, (255,255,255),(0,0),(650,0), 20)
    return limite

def quadra_iferior():
    limite = pygame.draw.line(screen, (255,255,255),(650,650),(0,650), 20)
    return limite
    
def gol_esquerda():
    limite = pygame.draw.line(screen, (255,255,255),(650,650),(0,650), 20)
    return limite
    
def gol_direita():
    limite = pygame.draw.line(screen, (255,255,255),(650,650),(0,650), 20)
    return limite

def ball(x,y):
    ball_pos = (x,y)
    ball = pygame.draw.circle(screen, (255,255,255), ball_pos, 10)
    return ball

x = 0
y = 0

direction_down = False
direction_up =False
direction_left =False
direction_right = False

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
    quadra_iferior()
    quadra_superior()
    player = player1(player_1_position_y)

    if direction_down and direction_up and direction_left and direction_right == False:
        x,y = 0,0
        
    if direction_down == True:
        y += 1
        direction_up = False
        
    elif direction_up == True:
        y -= 1
        direction_down = False

        
    if direction_right == True:
        x+=1
        direction_left = False
        
    elif direction_left == True:
        x-=1
        direction_right = False
        
        
        
        
    print(x,y)
    
    
    ball_ = ball(x,y)
    direction_down = True
    direction_right = True
    
    if ball_.colliderect(player):
            
        
        
        x = player_1_position_y
        print("colidiu") 
 
 
    pygame.display.flip()

    dt = clock.tick(60)

pygame.quit()

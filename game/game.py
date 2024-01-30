import pygame
from pygame.locals import *
from sys import exit



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


def ball():
    ball_pos = (300,300)
    ball = pygame.draw.circle(screen, (255,255,255), ball_pos, 10)
    return ball
player_1_position_y = 0

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            
            if event.key == K_w:
                player_1_position_y = player_1_position_y + 10
                
            if event.key == K_s:
                player_1_position_y = player_1_position_y - 10




    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    player1(player_1_position_y)
    ball()
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

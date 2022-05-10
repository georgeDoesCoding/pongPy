#Imports
from turtle import right
import pygame
from paddle import Paddle
from ball import Ball


pygame.init()
fps = pygame.time.Clock()


#CONSTANTS
#Screen settings
WIDTH = 800
HEIGHT = 500
#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
#Bat Settings
BAT_WIDTH = 10
BAT_HEIGHT = 60
#Ball Settings
BALL_RADIUS = 10


#Setting up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Create paddles and ball
left_paddle = Paddle(20,HEIGHT/2,BAT_WIDTH,BAT_HEIGHT,20+BAT_WIDTH)
right_paddle = Paddle(WIDTH-20-BAT_WIDTH,HEIGHT/2,BAT_WIDTH,BAT_HEIGHT,WIDTH-20-BAT_WIDTH)

ball = Ball(WIDTH/2, HEIGHT/2,-2,1,BALL_RADIUS)


#Game loop
running = True
while running:

    #Refreshing screen
    screen.fill(BLACK)

    #Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle.moveUp()
            if event.key == pygame.K_s:
                left_paddle.moveDown()
            if event.key == pygame.K_UP:
                right_paddle.moveUp()
            if event.key == pygame.K_DOWN:
                right_paddle.moveDown()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                left_paddle.vely=0
            if event.key == pygame.K_s:
                left_paddle.vely=0
            if event.key == pygame.K_UP:
                right_paddle.vely=0
            if event.key == pygame.K_DOWN:
                right_paddle.vely=0
                
    #Update and Draw paddles
    right_paddle.update(HEIGHT)
    left_paddle.update(HEIGHT)
    

    #Check collision
    ball.check_collision(left_paddle.bat_x,left_paddle.y,right_paddle.bat_x,right_paddle.y,WIDTH,HEIGHT,BAT_HEIGHT)

    ball.update()

    left_paddle.draw(screen,WHITE)
    right_paddle.draw(screen,WHITE)
    ball.draw(screen,WHITE)

    #Drawing table
    pygame.draw.line(screen,WHITE,(WIDTH/2,0),(WIDTH/2,HEIGHT))
    
    #Update screen
    pygame.display.flip()
    fps.tick(120)
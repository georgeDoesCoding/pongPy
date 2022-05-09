#Imports
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
left_paddle = Paddle(40,HEIGHT/2,BAT_WIDTH,BAT_HEIGHT)
right_paddle = Paddle(WIDTH-40-BAT_WIDTH,HEIGHT/2,BAT_WIDTH,BAT_HEIGHT)
ball = Ball(WIDTH/2, HEIGHT/2,0,0,BALL_RADIUS)


#Game loop
running = True
while running:

    #Refreshing screen
    screen.fill(BLACK)

    #Update and Draw Ball
    ball.update()
    ball.draw(screen,WHITE)


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



    #Draw paddles
    left_paddle.draw(screen,WHITE)
    right_paddle.draw(screen,WHITE)

    #Drawing table
    pygame.draw.line(screen,WHITE,(WIDTH/2,0),(WIDTH/2,HEIGHT))
    

    #Update screen
    pygame.display.flip()
    fps.tick(60)
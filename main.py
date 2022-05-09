import pygame
from paddle import Paddle

pygame.init()

#CONSTANTS
WIDTH = 800
HEIGHT = 500
BLACK = (0,0,0)
WHITE = (255,255,255)

#Setting up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)


#Create paddles
left_paddle = Paddle(40,HEIGHT/2)

#Game loop
running = True
while running:

    #Refreshing screen
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                left_paddle.moveUp()
            if event.key == pygame.K_w:
                left_paddle.moveDown()
            
    #Draw paddles
    left_paddle.draw(screen,WHITE)

    #Drawing table
    pygame.draw.line(screen,WHITE,(WIDTH/2,0),(WIDTH/2,HEIGHT))
    
   
    #Update screen
    pygame.display.flip()
     
    
    

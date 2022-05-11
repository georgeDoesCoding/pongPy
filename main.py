#Imports
from turtle import right
import pygame
from paddle import Paddle
from ball import Ball

pygame.init()
fps = pygame.time.Clock()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

BLACK = (0,0,0)
WHITE = (255,255,255)

BAT_WIDTH, BAT_HEIGHT = 10, 60
BALL_RADIUS = 10

#Create paddles and ball
left_paddle = Paddle(20,HEIGHT/2,BAT_WIDTH,BAT_HEIGHT,20+BAT_WIDTH)
right_paddle = Paddle(WIDTH-20-BAT_WIDTH,HEIGHT/2,BAT_WIDTH,BAT_HEIGHT,WIDTH-20-BAT_WIDTH)
ball = Ball(WIDTH/2, HEIGHT/2,-2,1,BALL_RADIUS)


score_2_win = 5
SCORE_FONT = pygame.font.SysFont("comicsans",50)

left_score = 0
right_score = 0

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

    if ball.x > WIDTH:
        left_score += 1
        ball.reset()
    if ball.x < 0:
        right_score += 1
        ball.reset()

    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    screen.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    screen.blit(right_score_text, (WIDTH * (3/4) -
                                right_score_text.get_width()//2, 20))
    
                
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
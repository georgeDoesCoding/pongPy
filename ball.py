import pygame

class Ball():
    def __init__(self,x,y,x_vel,y_vel,radius):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = radius


    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel


    def draw(self,screen,colour):
        pygame.draw.circle(screen,colour,(self.x, self.y), self.radius)
import pygame

class Paddle:
    def __init__(self,x,y,wide,tall):
        self.x = x
        self.y = y
        self.wide = wide
        self.tall = tall


    def moveUp(self):
        self.y -= 20


    def moveDown(self):
        self.y += 20


    def draw(self,screen,colour):
        pygame.draw.rect(screen,colour,(self.x,self.y,self.wide,self.tall))
import pygame

class Paddle:

    speed = 5
    WHITE = (255,255,255)

    def __init__(self,x,y,wide,tall,bat_x):
        #Top left position of bat
        self.x = x
        self.y = y
        #Dimensions
        self.wide = wide
        self.tall = tall
        self.vely = 0
        self.bat_x = bat_x
        
    def moveUp(self):
        self.vely = -self.speed
    def moveDown(self):
        self.vely = self.speed

    def update(self,screen_height):
        if self.y < 0:
            self.y = 0

        elif self.y > screen_height - self.tall:
            self.y = screen_height - self.tall
    
        else:
            self.y += self.vely


    def draw(self,screen,colour):
        pygame.draw.rect(screen,self.WHITE,(self.x,self.y,self.wide,self.tall))
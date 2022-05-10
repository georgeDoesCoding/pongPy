import pygame

class Paddle:
    def __init__(self,x,y,wide,tall,bat_x):
        #Top right position of bat
        self.x = x
        self.y = y
        #Dimensions
        self.wide = wide
        self.tall = tall
        #Current Velocity
        self.vely = 0
        #Bat interface x position
        self.bat_x = bat_x
        #Bat speed
        self.speed =5

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
        pygame.draw.rect(screen,colour,(self.x,self.y,self.wide,self.tall))
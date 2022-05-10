import pygame

class Ball():
    def __init__(self,x,y,x_vel,y_vel,radius):
        self.origin = (x,y)
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = radius

    def check_collision(self,x1,y1,x2,y2,wall,ceiling,bat_height):
        # X wall collisions
        if self.x <= 0:
            self.x_vel = -self.x_vel
            self.x, self.y = self.origin[0],self.origin[1]
        if self.x >= wall:
            self.x_vel = - self.x_vel
            self.x, self.y = self.origin[0],self.origin[1]

        # Y wall collisions
        if self.y -10 <= 0:
            self.y_vel = -self.y_vel
        if self.y + 10>= ceiling:
            self.y_vel = - self.y_vel
    
        #Left bat
        if self.x - 10 <= x1 and self.x + 10 >= x1 and self.y>y1-self.radius and self.y < y1+bat_height+self.radius:
            self.x_vel = -self.x_vel*1.02

            self.y_vel = (self.y - y1)*0.05*self.y_vel

        #Right bat
        if self.x + 10 >= x2 and self.x -10 <= x2 and self.y>y2-self.radius and self.y < y2+bat_height+self.radius:
            self.x_vel = -self.x_vel*1.02

            self.y_vel = (self.y - y2)*0.05*self.y_vel
        
    def update(self):
        if self.x_vel >= 10:
            self.x_vel = 10
        if self.y_vel >= 10:
            self.x_vel = 10

        self.x += self.x_vel
        self.y += self.y_vel


    def draw(self,screen,colour):
        pygame.draw.circle(screen,colour,(self.x, self.y), self.radius)
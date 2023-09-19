from functions import *
class Ball:
    color = None
    ballrect = None
    image = None
    row = None
    column = None
    def __init__(self, color, row,col):
        self.color = color
        self.image = pygame.image.load("images/" + self.color + ".png")
        self.ballrect = self.image.get_rect()
        self.row = row
        self.column = col

    #def ball_update(self):
     #   screen.blit(self.image, (self.pos_x,self.pos_y))

    def ball_delete(self):
        del self


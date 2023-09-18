from functions import *
class Ball:
    color = None
    ballrect = None
    image = None
    pos_x = None
    pos_y = None
    row = None
    column = None
    def __init__(self, color, pos_x,pos_y, row,col):
        self.color = color
        self.pos_x, self.pos_y = pos_x,pos_y
        self.image = pygame.image.load("images/" + self.color + ".png")
        self.ballrect = self.image.get_rect()
        self.row = row
        self.column = col

    #def ball_update(self):
     #   screen.blit(self.image, (self.pos_x,self.pos_y))

    def ball_delete(self):
        del self


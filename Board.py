from functions import random_color, initial_random_place
from Constants import *
from Ball import *
class Board:
    width = BOARD_7X7
    tile_no = None
    board_image_list = []
    board_color_list = []
    next_balls =[]
    next_taken_places = []
    def __init__(self,tile_no=7):
        self.tile_no = tile_no
        for y in range(self.tile_no):
            for x in range (self.tile_no):
                image = pygame.image.load("images/tile.png")
                self.board_color_list.append(0)
                self.board_image_list.append(image)
        #initial balls
        self.generate_balls(NO_NEXT_BALLS)


    def board_update(self):
        #check for 5 in row
        #remove them if so


        for y in range(self.tile_no):
            for x in range(self.tile_no):
                screen.blit(self.board_image_list[x + self.tile_no*y], (x*TILE_SIZE, y*TILE_SIZE))

    def generate_balls(self,how_many):
        for i in range(how_many):
            new_place = initial_random_place(self.tile_no, self.board_color_list, self.next_taken_places)
            ball = Ball(random_color(), new_place)

            self.next_taken_places.append(new_place)
            self.next_balls.append(ball)
            self.board_image_list[new_place] = ball.image
            self.board_color_list[new_place] = ball.color

    def check_if_empty(self,pos):
        if self.board_color_list[pos] == 0: return True
        else: return False

    def move_ball(self, old_pos, new_pos):
        if self.board_color_list[old_pos] != 0 and self.board_color_list[new_pos] == 0:
            self.board_color_list[new_pos] = self.board_color_list[old_pos]
            self.board_color_list[old_pos] = 0
            self.board_image_list[new_pos] = self.board_image_list[old_pos]
            self.board_image_list[old_pos] = pygame.image.load("images/tile.png")
            self.board_update()

    def same_color_around(self,ball):
        places = [ball.place - self.tile_no - 1, ball.place - self.tile_no,
                  ball.place - self.tile_no + 1, ball.place - 1,
                  ball.place + 1, ball.place + self.tile_no - 1,
                  ball.place + self.tile_no, ball.place + self.tile_no + 1]
        legal_places = places
        for i in places:
            if places[i] not in (0, 48):
                places[i] = -5
                legal_places[i].remove()

        for c in legal_places:
            if self.board_color_list[legal_places[c]] != ball.color:
                legal_places[c].remove()

        places = [i if places[i] in legal_places else -5 for i in places] # moze da sie usunac -5?
        return places



    def check_5_in_row(self, ball, counter=0):

        counter += 1
        possible_pairs = [ [dct['left_up'], dct['right_down']],
                           [dct['left'], dct['right']],
                           [dct['right_up'], dct['left_down']],
                           [dct['up'], dct['down']]]

        # check if the same color around
        directions = self.same_color_around(ball.place)

        directions = set(dct.keys()).intersection(directions)
        if not directions:
            return False, counter
        elif len(directions) > 1:
            for list in possible_pairs:
                if all(item in directions for item in list):
                    return 





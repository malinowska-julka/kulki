from functions import random_color, initial_random_place
from Constants import *
import copy
from Ball import *
class Board:
    width = BOARD_7X7
    tile_no = None
    board_image_list = []
    board_list = []
    next_balls = []
    next_taken_places = []
    balls_to_remove = []

    def __init__(self,tile_no=7):
        self.tile_no = tile_no
        for y in range(self.tile_no):
            for x in range (self.tile_no):
                image = pygame.image.load("images/tile.png")
                self.board_list.append(0)
                self.board_image_list.append(image)
        #initial balls
        self.generate_balls(NO_NEXT_BALLS)


    def board_update(self):

        for y in range(self.tile_no):
            for x in range(self.tile_no):
                screen.blit(self.board_image_list[x + self.tile_no*y], (x*TILE_SIZE, y*TILE_SIZE))

    def generate_balls(self,how_many):
        possible_places = self.board_list.count(0)
        if possible_places < how_many:
            how_many = possible_places

        for i in range(how_many):
            new_place, pos_x, pos_y = initial_random_place(self.tile_no, self.board_list, self.next_taken_places)
            ball = Ball(random_color(), new_place, pos_x, pos_y)

            self.next_taken_places.append(new_place)
            self.next_balls.append(ball)
            self.board_image_list[new_place] = ball.image
            self.board_list[new_place] = ball
            #self.check_5_in_row(ball)

    def check_if_empty(self,pos):
        if self.board_list[pos] == 0: return True
        else: return False

    def move_ball(self, old_pos, new_pos, position_new):
        if self.board_list[old_pos] != 0 and self.board_list[new_pos] == 0:
            self.board_image_list[new_pos] = self.board_image_list[old_pos]
            same_ball = Ball(self.board_list[old_pos].color,new_pos,position_new[0],position_new[1])

            self.remove_ball(self.board_list[old_pos])
            self.board_list[new_pos] = same_ball

            to_remove = self.check_5_in_row(self.board_list[new_pos])
            #possible_places = self.board_list.count(0)

            if to_remove:

                for i in self.balls_to_remove:
                    self.remove_ball(i)
                self.balls_to_remove = []

            self.board_update()


    def remove_ball(self,ball):
        p = ball.place
        self.board_image_list[p] = pygame.image.load("images/tile.png")
        f = self.board_list[p]
        ball.ball_delete
        self.board_list[p] = 0



    def get_one_direction_place(self, ball, direction):
        places = [ball.place - self.tile_no - 1, ball.place - self.tile_no,
                  ball.place - self.tile_no + 1, ball.place - 1,
                  ball.place + 1, ball.place + self.tile_no - 1,
                  ball.place + self.tile_no, ball.place + self.tile_no + 1]

        if places[direction[0]] in range(0,48):
            return [places[direction[0]]]

        else: return []

    def same_color_around(self, ball, one_direction = None):

        if not one_direction:
            places, directions = get_places_around(ball.pos_x, ball.pos_y)

        else:
            places = self.get_one_direction_place(ball, one_direction)
            directions = one_direction.copy()

        for c in range(len(places)):

            if self.board_list[places[c]] == 0 or self.board_list[places[c]].color != ball.color:
                places[c] = -5
                directions[c] = -5
        places = list(filter(lambda a: a != -5, places))
        directions = list(filter(lambda a: a != -5, directions))

        return places, directions


    def check_5_in_row(self, ball, check_dir=[]):


        self.balls_to_remove.append(ball)

        possible_pairs = [[0, 7],
                         [3, 4],
                         [2, 5],
                         [1, 6]]

        # check if the same color around
        if not check_dir:
            places, directions = self.same_color_around(ball)
        else:
            places, directions = self.same_color_around(ball, check_dir)


        if not directions or not places or self.board_list[places[0]] == 0:
            return False

        elif len(directions) > 1:
            for list in possible_pairs:
                if all(item in directions for item in list):
                    #dwie kulki
                    for i in range(len(list)):
                        f = self.balls_to_remove
                        b = list[i]
                        self.check_5_in_row(self.board_list[places[list[i]]], [list[i]])
        elif len(directions) == 1:
            self.check_5_in_row(self.board_list[places[0]], directions)

        if len(self.balls_to_remove) >= 3:
            return True

        else:
            self.balls_to_remove = []
            return False




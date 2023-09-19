from functions import random_color
from Constants import *
import random
import copy
import numpy as np

#TODO: TAKEN FIELD - nie generuj nowych kulek
#TODO: skanuj caly kwadrat z kulką w środku / a może caly board z danym kolorem?
#TODO: find pattern in square - row, column, cross left / cross right - skanuj całą tablicę po kolei, szukając patternu w kolorach
#TODO: extend square to search - check outer ball in square


class Board:
    width = BOARD_7X7
    tile_no = None
    board = []
    board_image = []
    next_balls = []
    next_taken_places = []
    balls_to_remove = []

    def __init__(self, tile_no=7):
        self.tile_no = tile_no

        self.board = [[0 for _ in range(tile_no)] for _ in range(tile_no)]
        image = pygame.image.load("images/tile.png")
        self.board_image = [[image for _ in range(tile_no)] for _ in range(tile_no)]
        #initial balls
        self.generate_balls(NO_NEXT_BALLS)

    def board_update(self):
        for x in range(self.tile_no):
            for y in range(self.tile_no):
                screen.blit(self.board_image[x][y], (y*TILE_SIZE, x*TILE_SIZE))

    def generate_balls(self, how_many):

        for i in range(how_many):

            place = random.choice(self.scan_board())
            color = random_color()

            self.board[place[0]][place[1]] = color

            image = pygame.image.load("images/" + color_dict[color] + ".png")
            self.board_image[place[0]][place[1]] = image

            '''to_remove = self.check_5_in_row(ball)
            if to_remove and len(self.balls_to_remove) >= 5:
                for i in self.balls_to_remove:
                    print(i.color, i.place)
                print('/n')
                for i in self.balls_to_remove:
                    self.remove_ball(i)

            self.balls_to_remove = []'''

    def check_if_empty(self, row, column):
        if self.board[row][column] == 0: return True
        else: return False

    def move_ball(self, row_old, col_old, row_new, col_new, position_new, turn):

        self.board_image[row_new][col_new] = self.board_image[row_old][col_old]
        self.board[row_new][col_new] = self.board[row_old][col_old]
        self.remove_ball(row_old, col_old)

        #self.check_5_in_row(self.board_list[new_pos])
        if turn > 1:
            p = self.board[row_old][col_old]
            r = self.board[row_new][col_new]
            print('d')

        #self.one_color_board(self.board[row_new][col_new])

        '''
            if to_remove:
                print("no balls to maybe remove")
                print(str(len(self.balls_to_remove)))
            if to_remove and len(self.balls_to_remove) >= 5:
                for i in self.balls_to_remove:
                    print(i.color, i.place)
                print('/n')
                for i in self.balls_to_remove:
                    self.remove_ball(i)'''

        self.balls_to_remove = []
        self.board_update()

    def remove_ball(self, row, column):
        r = row
        c = column
        self.board_image[r][c] = pygame.image.load("images/tile.png")
        self.board[r][c] = 0


    # def search_around(self, row, col): koncept kwadratów

    def one_color_board(self, color): # bez sensu - skanuj całą tablicę po kolei, szukając patternu w kolorach
        color_board = self.board.copy()
        for x in range(self.tile_no):
            for y in range(self.tile_no):
                if color_board[x][y] != 0:
                    if color_board[x][y].color == color:
                        color_board[x][y] = 1
                    else:
                        color_board[x][y] = 0
            print(color_board[x][:])

    def get_one_direction_place(self, ball, direction):
        places = [ball.place - self.tile_no - 1, ball.place - self.tile_no,
                  ball.place - self.tile_no + 1, ball.place - 1,
                  ball.place + 1, ball.place + self.tile_no - 1,
                  ball.place + self.tile_no, ball.place + self.tile_no + 1]

        if places[direction[0]] in range(0, 48):
            return [places[direction[0]]]

        else: return []

    '''def same_color_around(self, ball, one_direction = None):
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

        if places:
            print("next_checking:")
            for i in places:
                print(i)
        return places, directions'''


    def check_5_in_row(self, ball, check_dir=[], balls_in_rows = []):
        print("checking ball: " + ball.color + " " + str(ball.place))

        balls_in_rows.append(ball)

        #self.balls_to_remove.append(ball)
        possible_pairs = [[0, 7],
                         [3, 4],
                         [2, 5],
                         [1, 6]]

        # check if the same color around
        if not check_dir:
            places, directions = self.same_color_around(ball)
        else:
            places, directions = self.same_color_around(ball, check_dir)
        for i in directions:
            print("dir")
            print(i)

        if not directions or not places or self.board_list[places[0]] == 0:
            return

        '''elif len(directions) > 1:
            for list in possible_pairs:
                if all(item in directions for item in list):
                    counter = 0
                    #dwie kulki na skos
                    for i in range(len(list)):
                        place_idx = directions.index(list[i])
                        c = self.check_5_in_row(self.board_list[places[place_idx]], [list[i]], counter)
                        counter += c
                        directions.remove(list[i])
                    if counter >= 4:
                        count += counter
            #rozne kierunki
            if directions:
                for dir in directions:
                    c = self.check_5_in_row(self.board_list[directions.index(dir)], list(dir))
                    count += c

        elif len(directions) == 1:
            c = self.check_5_in_row(self.board_list[places[0]], directions)
            count += c

        return count'''

    def scan_board(self):
        free_places = []

        for y in range(self.tile_no):
            for x in range(self.tile_no):
                # look for pattern 5 in row
                if self.board[x][y] == 0:
                    free_places.append([x, y])

        return free_places

    # ogarnac county chyba lepiej zrobiccountery i sprawdzacczy 5+ i potemto do counta glowenego dac
    # zmienic gdzie dodawac kulki do balls_to_renmove
    # List[List[Optional[Ball]]] = [
#             [0 for _ in range(size)] for _ in range(size)
#         ]  print("row_new: " + str(row_new) + ", col_new: " + str(col_new))
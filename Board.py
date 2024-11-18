from functions import *
from Constants import *
from AStarCell import *
import random
import copy
import numpy as np


class Board:
    width = BOARD_7X7
    tile_no = None
    board = []
    board_image = []
    next_balls = []
    next_taken_places = []
    board_coors_up = (0, SIDE_MENU_HEIGHT)

    def __init__(self, tile_no=TILE_NO):
        self.tile_no = tile_no

        self.board = [[-1 for _ in range(tile_no)] for _ in range(tile_no)]
        image = pygame.image.load("images/tile.png")
        self.board_image = [[image for _ in range(tile_no)] for _ in range(tile_no)]
        # initial balls
        self.generate_balls(NO_NEXT_BALLS)
        self.add_balls()

    def board_update(self):

        for x in range(self.tile_no):
            for y in range(self.tile_no):
                screen.blit(
                    self.board_image[x][y],
                    (y * TILE_SIZE, x * TILE_SIZE + SIDE_MENU_HEIGHT),
                )

    def generate_balls(self, how_many):
        for i in range(how_many):
            self.next_taken_places.append(
                random.choice(
                    [
                        val
                        for val in self.scan_board()
                        if val not in self.next_taken_places
                    ]
                )
            )
            self.next_balls.append(random_color())

    def add_balls(self):
        for i in range(len(self.next_balls)):
            self.board[self.next_taken_places[i][0]][self.next_taken_places[i][1]] = (
                self.next_balls[i]
            )

            image = pygame.image.load(
                "images/" + color_dict[self.next_balls[i]] + ".png"
            )
            self.board_image[self.next_taken_places[i][0]][
                self.next_taken_places[i][1]
            ] = image

            to_remove = self.get_lines(
                self.next_taken_places[i][0], self.next_taken_places[i][1]
            )
            for line in to_remove:
                self.score_and_remove(line)
        self.next_taken_places = []
        self.next_balls = []

    def check_if_empty(self, row, column):

        if self.board[row][column] == -1:
            return True
        else:
            return False

    def move_ball(self, row_old, col_old, row_new, col_new, position_new, turn):
        self.board_image[row_new][col_new] = self.board_image[row_old][col_old]
        self.board[row_new][col_new] = self.board[row_old][col_old]
        self.remove_ball(row_old, col_old)

        to_remove = self.get_lines(row_new, col_new)

        for line in to_remove:
            self.score_and_remove(line)

        self.board_update()

    def remove_ball(self, row, column):
        r = row
        c = column
        self.board_image[r][c] = pygame.image.load("images/tile.png")
        self.board[r][c] = -1

    def get_lines(self, coor_y, coor_x):
        ball_color = self.board[coor_y][coor_x]
        lines = [
            [[coor_y, coor_x]],
            [[coor_y, coor_x]],
            [[coor_y, coor_x]],
            [[coor_y, coor_x]],
        ]  # horizontal, vertical, 2 diagonals
        l = r = u = d = lu = ld = ru = rd = ball_color
        i = 1
        while any([l, r, u, d, lu, ld, ru, rd]):

            # horizontal
            if coor_x - i >= 0 and l == self.board[coor_y][coor_x - i]:
                lines[0].append([coor_y, coor_x - i])
            else:
                l = 0
            if coor_x + i <= 6 and r == self.board[coor_y][coor_x + i]:
                lines[0].append([coor_y, coor_x + i])
            else:
                r = 0

            # vertical
            if coor_y - i >= 0 and u == self.board[coor_y - i][coor_x]:
                lines[1].append([coor_y - i, coor_x])
            else:
                u = 0
            if coor_y + i <= 6 and d == self.board[coor_y + i][coor_x]:
                lines[1].append([coor_y + i, coor_x])
            else:
                d = 0
            # diagonals
            if (
                coor_y + i <= 6
                and coor_x - i >= 0
                and ld == self.board[coor_y + i][coor_x - i]
            ):
                lines[2].append([coor_y + i, coor_x - i])
            else:
                ld = 0
            if (
                coor_y - i >= 0
                and coor_x + i <= 6
                and ru == self.board[coor_y - i][coor_x + i]
            ):
                lines[2].append([coor_y - i, coor_x + i])
            else:
                ru = 0

            if (
                coor_y - i >= 0
                and coor_x - i >= 0
                and lu == self.board[coor_y - i][coor_x - i]
            ):
                lines[3].append([coor_y - i, coor_x - i])
            else:
                lu = 0
            if (
                coor_y + i <= 6
                and coor_x + i <= 6
                and rd == self.board[coor_y + i][coor_x + i]
            ):
                lines[3].append([coor_y + i, coor_x + i])
            else:
                rd = 0
            i = i + 1

        score_lines = []
        for line in lines:
            if len(line) > 4:
                score_lines.append(line)
        return score_lines

    def score_and_remove(self, places):
        balls = len(places)
        # print("dlugosc: " + str(balls))
        # scoring formula -> total_score += score
        for place in places:
            # print("removing: " + str(place))
            self.remove_ball(place[0], place[1])

    def scan_board(self):
        for color in color_dict:
            free_places = []
            color_places = []
            for y in range(self.tile_no):
                for x in range(self.tile_no):
                    # look for pattern 5 in row
                    if self.board[x][y] == color:
                        color_places.append([x, y])

                    # self.board_update()
                    if self.board[x][y] == -1:
                        free_places.append([x, y])
            # self.pattern_search(color_places)
        return free_places

    def path_check(self, src, dest):
        source = Cell(src[0], src[1])
        open = [source]
        closed = []
        path_found = False

        while open:
            q = find_min_f(open)
            open.remove(q)
            succ = []
            directions = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]
            for dir in directions:

                new_r = q.row + dir[0]
                new_c = q.col + dir[1]

                if is_valid(new_r, new_c) and self.check_if_empty(new_r, new_c):
                    new_s = Cell(new_r, new_c)
                    new_s.assign_parent(q.row, q.col)
                    succ.append(new_s)

            for s in succ:

                if (s.row == dest[0]) and (s.col == dest[1]):
                    path_found = True
                    return path_found

                else:
                    s.g = q.g + 1.0
                    s.h = calculate_distance(s.row, s.col, dest[0], dest[1])
                    s.f = s.g + s.h
                find = False
                for c in open:
                    if (c.row == s.row) and (c.col == s.col) and (c.f < s.f):
                        find = True
                        break
                if not find:
                    all_good = True
                    for c in closed:
                        if (c.row == s.row) and (c.col == s.col) and (c.f < s.f):
                            all_good = False
                            break

                    if all_good:
                        open.append(s)

            closed.append(q)

        return path_found

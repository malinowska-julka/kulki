import sys, pygame, random,time
from functions import *
from Board import *
import time


def one_turn(position):
    row_old, col_old = get_place_from_mouse(position[0])
    if board.check_if_empty(row_old, col_old):
        display_text('IT IS AN EMPTY FIELD!', font, display_surface)
        return -1
    row_new, col_new = get_place_from_mouse(position[1])
    if not board.check_if_empty(row_new, col_new):
        display_text('IT IS A TAKEN FIELD!', font, display_surface)
        return -1
    else:
        board.move_ball(row_old, col_old, row_new, col_new, position[1])


pygame.init()
font = pygame.font.Font('Museo_Slab_500_2.otf',32)
display_surface = pygame.display.set_mode((width, height))

board = Board()
mouse_click = 0
positions = []
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_click < 2:
                positions.append(pygame.mouse.get_pos())
                mouse_click += 1

    board.board_update()
    pygame.display.flip()

    '''isEmpty = board.scan_board
    if isEmpty:
        time.sleep(2)
        sys.exit()'''

    if mouse_click == 1:
        row, col = get_place_from_mouse(positions[0])
        if board.check_if_empty(row, col):
            display_text('IT IS AN EMPTY FIELD!', font, display_surface)
            mouse_click = 0
            positions = []


    if mouse_click == 2:
        one_turn(positions)

        '''possible_places = board.count(0)

        if possible_places > 0:
            if possible_places > 15:
                board.generate_balls(14)
            else:
                board.generate_balls(possible_places)'''

        mouse_click = 0
        positions = []

    pygame.event.pump()

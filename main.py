import sys, pygame, random, time
from functions import *
from Board import *
from SideMenu import *
import time


def one_turn(position, turn):
    row_old, col_old = get_place_from_mouse(position[0])
    row_new, col_new = get_place_from_mouse(position[1])

    if board.path_check([row_old, col_old], [row_new, col_new]):
        board.move_ball(row_old, col_old, row_new, col_new, position[1], turn)

        free_places = board.scan_board()
        if len(free_places) >= NO_NEXT_BALLS:
            board.generate_balls(NO_NEXT_BALLS)
        else:
            board.generate_balls(len(free_places))
    else:
        display_text("PATH NOT FOUND", font, display_surface)
        return -1


if __name__ == "__main__":
    pygame.init()
    font = pygame.font.Font("Museo_Slab_500_2.otf", 32)
    display_surface = pygame.display.set_mode((width, height))
    color = (255, 255, 255)
    display_surface.fill(color)

    board = Board()
    menu = SideMenu()
    mouse_click = 0
    positions = []
    turn = 0
    while True:
        for event in pygame.event.get():
            if len(board.scan_board()) == 0:
                display_text("THE END!!!", font, display_surface)
                time.sleep(2)
                sys.exit()

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_click < 2:
                    positions.append(pygame.mouse.get_pos())
                    mouse_click += 1

        board.board_update()
        menu.menu_update()
        pygame.display.flip()

        if mouse_click == 1:
            row, col = get_place_from_mouse(positions[0])
            if board.check_if_empty(row, col):
                display_text("IT IS AN EMPTY FIELD!", font, display_surface)
                mouse_click = 0
                positions = []

        if mouse_click == 2:
            row_n, col_n = get_place_from_mouse(positions[1])
            if not board.check_if_empty(row_n, col_n):
                positions[0] = positions[1]
                positions.pop()
                mouse_click -= 1
            else:
                turn += 1
                one_turn(positions, turn)
                mouse_click = 0
                positions = []

        pygame.event.pump()

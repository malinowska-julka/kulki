import pygame, time
import random

# from main import *
from Constants import *


def random_color():
    c = random.randint(1, 5)
    return c


def get_place_from_mouse(mouse_pos):

    row = (mouse_pos[1] - SIDE_MENU_HEIGHT) // TILE_SIZE
    column = mouse_pos[0] // TILE_SIZE

    return row, column


def display_text(text, font, display_surface):
    text_empty = font.render(text, True, white, warning_red)
    textrect = text_empty.get_rect()
    textrect.center = (width // 2, height // 2)

    display_surface.blit(text_empty, textrect)
    pygame.display.flip()
    time.sleep(1)


def get_places_around(pos_x, pos_y):
    positions = [
        (pos_x - TILE_SIZE, pos_y - TILE_SIZE),
        (pos_x, pos_y - TILE_SIZE),
        (pos_x + TILE_SIZE, pos_y - TILE_SIZE),
        (pos_x - TILE_SIZE, pos_y),
        (pos_x + TILE_SIZE, pos_y),
        (pos_x - TILE_SIZE, pos_y + TILE_SIZE),
        (pos_x, pos_y + TILE_SIZE),
        (pos_x + TILE_SIZE, pos_y + TILE_SIZE),
    ]
    directions = []
    for i in range(len(positions)):
        if positions[i][0] in range(0, BOARD_7X7) and positions[i][1] in range(
            0, BOARD_7X7
        ):
            positions[i] = get_place_from_mouse(positions[i])
            directions.append(i)
        else:
            positions[i] = -5
    positions = list(filter(lambda a: a != -5, positions))

    return positions, directions


def find_min_f(c_list):  # move to functions?
    min = c_list[0]
    for c in c_list:
        if c.f < min.f:
            min = c
    return min


def is_valid(r, c):
    return (r >= 0) and (r <= TILE_NO - 1) and (c >= 0) and (c <= TILE_NO - 1)


def calculate_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


# TODO co jak nie ma miejsca
# TODO scoring method
# TODO side menu z wynikiem
# TODO menu?
# TODO zrobic cos z komunikatami

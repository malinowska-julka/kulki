import pygame, time
import random
#from main import *
from Constants import *


def initial_random_place(board_size, balls_mash, next_balls):
    isFree = False
    while isFree == False:
        place = random.randint(0,pow(board_size,2)-1)
        row = random.randint(0,board_size-1)
        column = random.randint(0,board_size-1)

        if balls_mash[row][column] == 0:
            coor_x = BALL_SIZE * (place % board_size)
            coor_y = BALL_SIZE * (place//board_size)
            return coor_x, coor_y, row, column

def random_color():
    c = color_dict[random.randint(1, 5)]
    return c

def get_place_from_mouse(mouse_pos):

    row = mouse_pos[1] // TILE_SIZE
    column = mouse_pos[0] // TILE_SIZE

    return row, column

def display_text(text, font,display_surface):
    text_empty = font.render(text, True, white, warning_red)
    textrect = text_empty.get_rect()
    textrect.center = (width // 2, height // 2)

    display_surface.blit(text_empty, textrect)
    pygame.display.flip()
    time.sleep(1)

def get_places_around(pos_x,pos_y):
    positions = [(pos_x - TILE_SIZE, pos_y - TILE_SIZE),(pos_x, pos_y - TILE_SIZE),(pos_x + TILE_SIZE, pos_y - TILE_SIZE),
              (pos_x - TILE_SIZE, pos_y), (pos_x + TILE_SIZE, pos_y),
              (pos_x - TILE_SIZE, pos_y + TILE_SIZE), (pos_x, pos_y + TILE_SIZE), (pos_x + TILE_SIZE, pos_y + TILE_SIZE)
              ]
    directions = []
    for i in range(len(positions)):
        if positions[i][0] in range(0,BOARD_7X7) and positions[i][1] in range(0,BOARD_7X7):
            positions[i] = get_place_from_mouse(positions[i])
            directions.append(i)
        else:
            positions[i] = -5
    positions =list(filter(lambda a: a != -5, positions))

    return positions, directions






#todo co jak nie ma miejsca
#todo nie przechodzily przez inne kulki

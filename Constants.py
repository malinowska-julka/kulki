import pygame
TILE_SIZE = 120
BALL_SIZE = 120
BOARD_7X7 = TILE_SIZE*7
NO_NEXT_BALLS = 3
size = width, height = BOARD_7X7, BOARD_7X7
screen = pygame.display.set_mode(size)



warning_red = (92,13,13)
white = (255,255,255)
dct = {
    0: "left_up",
    1: "up",
    2: "right_up",
    3: "left",
    4: "right",
    5: "left_down",
    6: "down",
    7:  "right_down"
}

color_dict = {
    1 : "blue",
    2 : "green",
    3 : "orange",
    4 : "red",
    5 : "yellow"
}
from functions import *
from Constants import *


class SideMenu:
    height = SIDE_MENU_HEIGHT
    next_balls = []
    score = None
    font = None

    def __init__(self):
        # self.next_balls = [1, 2, 3]
        self.font = pygame.font.Font("Museo_Slab_500_2.otf", 42)
        self.score = 0

    def menu_update(self):

        for i, ball in enumerate(self.next_balls):
            image = pygame.image.load("images/next_balls/" + color_dict[ball] + ".png")
            screen.blit(
                image,
                (650 + i * NEXT_BALL_SIZE, 10),
            )
            text = self.font.render(str(self.score), True, "black")
            screen.blit(text, (360, 10))


# przekazywanie next_balls
# przyciski exit
# printowanie wynikow

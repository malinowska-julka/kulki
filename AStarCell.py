class Cell:
    row = None
    col = None
    parent_r = 0
    parent_c = 0
    f = None
    g = None
    h = None

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.f = 0
        self.g = 0
        self.h = 0

    def assign_parent(self, row, col):
        self.parent_r = row
        self.parent_c = col

import pygame
class Cell:
    color = (200, 200, 200)
    #       top    right bottom left
    def __init__(self, _window, _x, _y, _w, _h, _indexX, _indexY):
        self.x = _x
        self.y = _y
        self.w = _w
        self.h = _h
        self.window = _window
        self.indexX = _indexX
        self.indexY = _indexY
        self.walls = [True, True, True, True]
        self.visited = False

    def draw(self):
        # top wall
        if self.walls[0] == True:
            pygame.draw.line(self.window, self.color, (self.x, self.y), (self.x+self.w, self.y))
        # right wall
        if self.walls[1] == True:
            pygame.draw.line(self.window, self.color, (self.x+self.w, self.y), (self.x+self.w, self.y+self.h))
        #bottom wall
        if self.walls[2] == True:
            pygame.draw.line(self.window, self.color, (self.x, self.y+self.h), (self.x+self.w, self.y+self.h))
        # left wall
        if self.walls[3] == True:
            pygame.draw.line(self.window, self.color, (self.x, self.y), (self.x, self.y+self.h))

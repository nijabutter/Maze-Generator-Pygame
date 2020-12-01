'''
Requires pygame:
    From CLI:
    pip install pygame
    python -m pip install pygame
'''

import pygame
import random
import time
from Cell import Cell

W_WIDTH, W_HEIGHT = 500, 500 # does affect complexity just the size of each cell
ACROSS = DOWN = 20 # how many cells x and y DOES affect complexity
C_WIDTH, C_HEIGHT = W_WIDTH // ACROSS, W_HEIGHT // DOWN
window = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
pygame.display.set_caption("Maze")
isRunning = True
background = (0, 0, 0)
pygame.init()

cells = []
stack = []
current = None
unvisited = ACROSS * DOWN
def Setup():
    global cells
    global stack
    global current
    global unvisited
    cells = []
    stack = []
    current = None
    unvisited = ACROSS * DOWN
    for y in range(DOWN):
        ylist = []
        for x in range(ACROSS):
            ylist.append(Cell(window, x*C_WIDTH, y*C_HEIGHT, C_WIDTH, C_HEIGHT, x, y))
        cells.append(ylist)
    current = cells[0][0]
    unvisited -= 1


        


def Update():
    global current
    global unvisited
    global isRunning
    current.visited = True
    neighbours = []
    if current.indexX > 0:
        # can have left neighbour
        if cells[current.indexY][current.indexX-1].visited == False:
            neighbours.append(cells[current.indexY][current.indexX-1])

    if current.indexX < ACROSS-1:
        # can have right neighbour
        if cells[current.indexY][current.indexX+1].visited == False:
            neighbours.append(cells[current.indexY][current.indexX+1])
    
    if current.indexY > 0:
        # can have top neighbour
        if cells[current.indexY-1][current.indexX].visited == False:
            neighbours.append(cells[current.indexY-1][current.indexX])

    if current.indexY < DOWN-1:
        # can have bottom neighbour
        if cells[current.indexY+1][current.indexX].visited == False:
            neighbours.append(cells[current.indexY+1][current.indexX])
    
    # current cell has unvisited neighbours
    if len(neighbours) > 0:
        nextCell = neighbours[random.randint(0, len(neighbours)-1)]
        stack.append(current)
        nextCell.visited = True
        unvisited -= 1
        xDiff = current.indexX - nextCell.indexX
        yDiff = current.indexY - nextCell.indexY
        
        if xDiff == 1:
            # neighbour on left
            current.walls[3] = False
            nextCell.walls[1] = False
        elif xDiff == -1:
            # neighbour on right
            current.walls[1] = False
            nextCell.walls[3] = False
        if yDiff == 1:
            # neighbour on top
            current.walls[0] = False
            nextCell.walls[2] = False
        elif yDiff == -1:
            # neighbour on bottom
            current.walls[2] = False
            nextCell.walls[0] = False
        current = nextCell
    elif len(stack) > 0:
        current = stack.pop()

def MakeMaze():
    print("Making maze...")
    start = time.process_time()
    Setup()
    global unvisited
    while unvisited > 0:
        Update()
    print("Made maze in:", time.process_time() - start)

def Input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global isRunning
            isRunning = False
        elif event.type == pygame.KEYUP:
            MakeMaze()
    
def Draw():
    window.fill(background)
    for y in range(DOWN):
        for x in range(ACROSS):
            cells[y][x].draw()
            if x == 0 and y == 0:
                filled_rect = pygame.Rect(cells[y][x].x, cells[y][x].y, C_WIDTH, C_HEIGHT)
                pygame.draw.rect(window, (0, 100, 0), filled_rect) 
            elif x == ACROSS-1 and y == DOWN-1:
                filled_rect = pygame.Rect(cells[y][x].x, cells[y][x].y, C_WIDTH, C_HEIGHT)
                pygame.draw.rect(window, (100, 0, 0), filled_rect)
    pygame.display.flip()
MakeMaze()
while isRunning:
    Input()
    Draw()
    pygame.time.delay(32) # cap fps
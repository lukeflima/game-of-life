import numpy as np
import time
import os

def get_nei_num(index):
    return np.sum(grid[index[0]-1:index[0]+2,index[1]-1:index[1]+2]) - grid[index[0], index[1]]


def get_next_status(index_and_nei):
    alive = index_and_nei[0]
    num_nei = index_and_nei[1]
    #print(alive, num_nei)
    if alive:
        if num_nei < 2:
            return 0
        elif num_nei >= 2 and num_nei <= 3:
            return 1
        elif num_nei > 3:
            return 0
    elif not alive:
        if num_nei == 3:
            return 1
    return alive


def get_next_grid(grid):
    list_indexes = [[[i,j] for j in range(HEIGHT)] for i in range(WIDTH)]
    num_nei = np.array([list(map(get_nei_num, x)) for x in list_indexes])
    next_grid = np.array([list(map(get_next_status, x)) for x in [[[grid[i,j], num_nei[i,j]] for j in range(HEIGHT)] for i in range(WIDTH)]])
    return next_grid


def genarate_random_grid():
    return np.round(np.random.random([WIDTH,HEIGHT])).astype('int')

                                                     
rows, columns = os.popen('stty size', 'r').read().split()
WIDTH, HEIGHT = int(rows), int(columns)

grid = genarate_random_grid()
try:
    os.system('clear')
    time.sleep(0.5)
    while True:
        rows, columns = os.popen('stty size', 'r').read().split()
        WIDTH_new, HEIGHT_new = int(rows), int(columns)
        if WIDTH_new != WIDTH or HEIGHT_new != HEIGHT:
            os.system('clear')
            WIDTH, HEIGHT = WIDTH_new, HEIGHT_new
            grid = genarate_random_grid()
            time.sleep(1)
        os.system('clear')
        grid_print = grid.copy().astype('str')
        grid_print[grid_print == '1'] = '#'
        grid_print[grid_print == '0'] = ' '
        print('\n'.join([''.join(x.tolist()) for x in grid_print]))
        grid = get_next_grid(grid)
        time.sleep(1.0/30)
finally:
    os.system('clear')
    import sys
    sys.exit(0)

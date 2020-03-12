import numpy as np
import time
import os
import terminalsize
import platform

'''
Returns a list with the number of neighbors of each cell
'''
def get_neighbors_num(cell):
    return np.sum(grid[cell[0]-1:cell[0]+2,cell[1]-1:cell[1]+2]) - grid[cell[0], cell[1]]

'''
Return the next state of the cell
'''
def get_next_status(cell_and_neighbors):
    alive = cell_and_neighbors[0]
    num_neighbors = cell_and_neighbors[1]
    #print(alive, num_neighbors)
    if alive:
        if num_neighbors < 2:
            return 0
        elif num_neighbors >= 2 and num_neighbors <= 3:
            return 1
        elif num_neighbors > 3:
            return 0
    elif not alive:
        if num_neighbors == 3:
            return 1
    return alive

'''
Return the next grid
'''
def get_next_grid(grid):
    list_cells = [[[i,j] for j in range(HEIGHT)] for i in range(WIDTH)]
    num_neighbors = np.array([list(map(get_neighbors_num, x)) for x in list_cells])
    next_grid = np.array([list(map(get_next_status, x)) for x in [[[grid[i,j], num_neighbors[i,j]] for j in range(HEIGHT)] for i in range(WIDTH)]])
    return next_grid

'''
Return a new random grid
'''
def genarate_random_grid():
    return np.round(np.random.random([WIDTH,HEIGHT])).astype('int')

def clear_screan():
    current_os = platform.system()
    if current_os == 'Windows':
        os.system('cls')
    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        os.system('clear')

# Get size of terminal
HEIGHT, WIDTH = terminalsize.get_terminal_size()

grid = genarate_random_grid()

# Try and finally for nice exit when CTRL + C
try:
    clear_screan()
    time.sleep(0.5)
    while True:
        # Update size and genarate new grid when terminal resizes
        HEIGHT_new, WIDTH_new = terminalsize.get_terminal_size()
        if WIDTH_new != WIDTH or HEIGHT_new != HEIGHT:
            clear_screan()
            WIDTH, HEIGHT = WIDTH_new, HEIGHT_new
            grid = genarate_random_grid()
            time.sleep(0.5)

        # Get grid ready to print
        grid_print = grid.copy().astype('str')
        grid_print[grid_print == '1'] = '#'
        grid_print[grid_print == '0'] = ' '

        # Clear screen
        clear_screan()
        
        print('\n'.join([''.join(x.tolist()) for x in grid_print]))

        grid = get_next_grid(grid)

        time.sleep(1.0/30)
finally:
    # Clean exit
    clear_screan()
    import sys
    sys.exit(0)

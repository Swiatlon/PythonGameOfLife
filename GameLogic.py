import random
import copy

# Constants
ROWS, COLS = 50, 50

class GameLogic:
    @staticmethod
    def initialize_grid():
        return [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]

    @staticmethod
    def get_neighbors(grid, x, y):
        neighbors = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_x, new_y = x + i, y + j
                if 0 <= new_x < ROWS and 0 <= new_y < COLS:
                    neighbors.append(grid[new_x][new_y])

        return neighbors
    
    @staticmethod
    def evolve(grid):
        new_grid = copy.deepcopy(grid)

        for i in range(ROWS):
            for j in range(COLS):
                neighbors = GameLogic.get_neighbors(grid, i, j)
                live_neighbors = sum(neighbors)
                current_cell = grid[i][j]

                 # Apply the rules of Conway's Game of Life
                if current_cell == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    new_grid[i][j] = 0  # Cell dies
                elif current_cell == 0 and live_neighbors == 3:
                    new_grid[i][j] = 1  # Cell becomes alive

        return new_grid
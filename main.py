from sudokusolver import *
import copy

if __name__ == "__main__":
    example = [
        [9, 0, 3, 0, 0, 8, 0, 0, 5],
        [0, 8, 2, 3, 1, 9, 0, 0, 0],
        [4, 1, 7, 0, 0, 0, 9, 0, 0],
        [0, 7, 0, 0, 9, 1, 0, 5, 3],
        [0, 5, 0, 2, 0, 7, 0, 8, 0],
        [1, 4, 0, 8, 3, 0, 0, 9, 0],
        [0, 0, 5, 0, 0, 0, 3, 2, 1],
        [0, 0, 0, 9, 7, 3, 5, 4, 0],
        [6, 0, 0, 1, 0, 0, 8, 0, 9]
    ]

    backtracking_solution = solve_sudoku_using_backtracking(copy.deepcopy(example))
    simulated_annealing_solution = solve_sudoku_using_simulated_annealing(copy.deepcopy(example))
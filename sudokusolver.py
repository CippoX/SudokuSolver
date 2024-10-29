from sudokutilityfunctions import *
from backtrackingutility import *
from simulatedannealingutility import *
import random

def solve_sudoku_using_backtracking(sudoku):
    sudoku = initialize_sudoku_domain(sudoku)
    sudoku = ac_3(sudoku)
    sudoku, _ = backtracking(sudoku)
    sudoku = format_sudoku(sudoku)
    sudoku_pretty_print(sudoku)

    return sudoku


def solve_sudoku_using_simulated_annealing(sudoku):
    sudoku = simulated_annealing(sudoku)
    sudoku_pretty_print(sudoku)

    return sudoku



def initialize_sudoku_domain(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                sudoku[i][j] = {1,2,3,4,5,6,7,8,9}
            else:
                sudoku[i][j] = {sudoku[i][j]}
    return sudoku



def format_sudoku(sudoku):
    sudoku_aux = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(sudoku[i][j].pop())

        sudoku_aux.append(row)

    return sudoku_aux



def ac_3(sudoku):
    while True:
        sudoku, update_operations = propagate_sudoku_constraint(sudoku)
        if update_operations == 0:
            break
    return sudoku



def backtracking(sudoku):
    if is_sudoku_solved(sudoku):
        return sudoku, True

    i, j = select_unassigned_variable(sudoku)

    for n in sudoku[i][j]:
        is_sudoku_valid = check_cell_domain(sudoku, i, j, n)

        if is_sudoku_valid:
            cell_aux = sudoku[i][j]
            sudoku[i][j] = {n}
            sudoku, result = backtracking(sudoku)

            if result:
                return sudoku, True
            else:
                sudoku[i][j] = cell_aux

    return sudoku, False



def simulated_annealing(sudoku):
    known_values_matrix = initialize_known_values_matrix(sudoku)
    t = choose_starting_temperature(copy.deepcopy(sudoku))
    sudoku = generate_random_state(copy.deepcopy(sudoku))
    prev_cost, stall_counter = 0, 0

    while True:
        candidate = generate_candidates(sudoku, known_values_matrix)

        current_state_cost = cost_function(sudoku)
        candidate_cost = cost_function(candidate)

        if candidate_cost == 0:
            return candidate

        if stall_counter == 120 or (current_state_cost < 2 and current_state_cost % 2 == 1):
            t += 1.5
            stall_counter = 0

        if random.uniform(0, 1) < calculate_p(current_state_cost, candidate_cost, t):
            sudoku = candidate
            if candidate_cost == prev_cost:
                stall_counter += 1
            else:
                stall_counter = 0

        t *= 0.999
        prev_cost = current_state_cost





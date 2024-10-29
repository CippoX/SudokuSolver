import random
import statistics
import copy
import math

def generate_random_state(sudoku):
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            occurrences = {1, 2, 3, 4, 5, 6, 7, 8, 9}

            for i in range(3):
                for j in range(3):
                    cell_value = sudoku[box_row + i][box_col + j]
                    if cell_value != 0:
                        occurrences.discard(cell_value)

            for i in range(3):
                for j in range(3):
                    if sudoku[box_row + i][box_col + j] == 0:
                        rand = random.choice(list(occurrences))
                        sudoku[box_row + i][box_col + j] = rand
                        occurrences.remove(rand)

    return sudoku



def cost_function(sudoku):
    cost = 0
    for i in range(9):
        row_duplicates = [0,0,0,0,0,0,0,0,0,0]
        column_duplicates = [0,0,0,0,0,0,0,0,0,0]

        for j in range(9):
            row_duplicates[sudoku[i][j]] += 1
            column_duplicates[sudoku[j][i]] += 1

        for n in range(10):
            if row_duplicates[n] > 1:
                cost += 1

            if column_duplicates[n] > 1:
                cost += 1

    return cost



def initialize_known_values_matrix(sudoku):
    known_values_matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                known_values_matrix[i][j] = 1

    return known_values_matrix


def pick_two_random_cells(known_values_matrix):
    base_row = random.choice([0, 3, 6])
    base_col = random.choice([0, 3, 6])

    i = base_row + random.randint(0, 2)
    j = base_col + random.randint(0, 2)

    while known_values_matrix[i][j] == 1:
        i = base_row + random.randint(0, 2)
        j = base_col + random.randint(0, 2)

    k = base_row + random.randint(0, 2)
    l = base_col + random.randint(0, 2)

    while known_values_matrix[k][l] == 1 and not(i == k and j == l):
        k = base_row + random.randint(0, 2)
        l = base_col + random.randint(0, 2)


    return i, j, k, l



def choose_starting_temperature(sudoku):
    list_of_differences = []
    for _ in range(10):
        aux = generate_random_state(copy.deepcopy(sudoku))
        list_of_differences.append(cost_function(aux))
    return statistics.pstdev(list_of_differences)



def generate_candidates(current_state, known_values_matrix):
    i, j, k, l = pick_two_random_cells(known_values_matrix)
    candidate = copy.deepcopy(current_state)
    candidate[i][j], candidate[k][l] = candidate[k][l], candidate[i][j]

    return candidate


def calculate_p(current_state_cost, candidate_cost, t):
    delta = candidate_cost - current_state_cost
    return math.exp(-delta / t)
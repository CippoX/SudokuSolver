import copy

def is_sudoku_solved(sudoku):
    for i in range(9):
        for j in range(9):
            if len(sudoku[i][j]) != 1:
                return False
    return True


def select_unassigned_variable(sudoku):
    for i in range(9):
        for j in range(9):
            if len(sudoku[i][j]) != 1:
                return i, j

'''
def select_unassigned_variable(sudoku):
    i, j = 10, 10
    min_domain_size = 10

    for k in range(9):
        for l in range(9):
             if len(sudoku[k][l]) < min_domain_size and len(sudoku[k][l]) != 1:
                i, j = k, l
                min_domain_size = len(sudoku[k][l])
    return i, j
'''

def check_cell_domain(sudoku, i, j, value):
    cell_aux = copy.deepcopy(sudoku[i][j])
    sudoku[i][j] = {value}
    result = (check_row_domain(sudoku, i, j, value) and
            check_column_domain(sudoku, i, j, value) and
            check_box_domain(sudoku, i, j, value))

    sudoku[i][j] = cell_aux
    return result



def check_row_domain(sudoku, row, j, value):
    for k in range(9):
        if value in sudoku[row][k] and k != j and len(sudoku[row][k]) == 1:
            return False
    return True



def check_column_domain(sudoku, i, column, value):
    for k in range(9):
        if value in sudoku[k][column] and k != i and len(sudoku[k][column]) == 1:
            return False
    return True



def check_box_domain(sudoku, i, j, value):
    box_col_start = (i // 3) * 3
    box_row_start = (j // 3) * 3

    for k in range(box_col_start, box_col_start + 3):
        for l in range(box_row_start, box_row_start + 3):
            if value in sudoku[k][l] and k != i and l != j and len(sudoku[k][l]) == 1:
                return False
    return True



def count_occurrences(sudoku):
    occurrences = [99,0,0,0,0,0,0,0,0,0]

    for i in range(9):
        for j in range(9):
            if len(sudoku[i][j]) == 1:
                occurrences[(next(iter(sudoku[i][j])))] += 1

    print(occurrences)
    return occurrences


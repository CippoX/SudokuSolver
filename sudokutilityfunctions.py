def propagate_sudoku_constraint(sudoku):
    update_operations = 0
    for i in range(9):
        for j in range(9):
            if len(sudoku[i][j]) == 1:
                sudoku, updates = update_cell_domain(sudoku, i, j, next(iter(sudoku[i][j])))
                update_operations += updates
    return sudoku, update_operations



def update_cell_domain(sudoku, i, j, value):
    sudoku, row_updates = update_row_domain(sudoku, i, j, value)
    sudoku, column_updates = update_column_domain(sudoku, i, j, value)
    sudoku, box_updates = update_box_domain(sudoku, i, j, value)

    return sudoku, row_updates + column_updates + box_updates



def update_row_domain(sudoku, row, j, value):
    updates = 0
    for k in range(9):
        if value in sudoku[row][k] and k != j:
            sudoku[row][k].remove(value)
            updates += 1
    return sudoku, updates



def update_column_domain(sudoku, i, column, value):
    updates = 0
    for k in range(9):
        if value in sudoku[k][column] and k != i:
            sudoku[k][column].remove(value)
            updates += 1
    return sudoku, updates



def update_box_domain(sudoku, i, j, value):
    updates = 0
    box_col_start = (i // 3) * 3
    box_row_start = (j // 3) * 3

    for k in range(box_col_start, box_col_start + 3):
        for l in range(box_row_start, box_row_start + 3):
            if value in sudoku[k][l] and k != i and l != j:
                sudoku[k][l].remove(value)
                updates += 1
    return sudoku, updates



def sudoku_pretty_print(sudoku):
    for i, row in enumerate(sudoku):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        row_str = ""
        for j, cell in enumerate(row):

            if j % 3 == 0 and j != 0:
                row_str += "| "

            if isinstance(cell, set):
                cell_str = " "
            else:
                cell_str = str(cell)

            row_str += cell_str + " "

        print(row_str.strip())
    print("\n")
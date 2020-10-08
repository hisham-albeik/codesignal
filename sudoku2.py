def sudoku2(grid):
    print(grid)
    for r in range(9):
        for c in range(9):
            if grid[r][c] != '.':
                number = grid[r][c]
                # Is there a duplicate in the row?
                if grid[r].count(number) != 1:
                    return False
                # Is there a duplicate in the column?
                for row in range(9):
                    if row == r:
                        continue
                    if grid[row][c] == number:
                        return False
                # Is there a duplicate in the cell
                cell_block_row = int(r/3)
                cell_block_col = int(c/3) * 3
                cell_id = cell_block_row + cell_block_col
                for sub_cell_row in range(3):
                    for sub_cell_col in range(3):
                        checking_cell_row = sub_cell_row + (3 * cell_block_row)
                        checking_cell_col = sub_cell_col + (cell_block_col)
                        if grid[checking_cell_row][checking_cell_col] == number and not (checking_cell_col == c and checking_cell_row == r):
                            return False

    return True

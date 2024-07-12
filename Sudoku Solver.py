def is_move_valid(grid, row, col, num):
    # Check if the number is already in the given row or column
    if num in grid[row]:
        return False
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check if the number is in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve(grid, row=0, col=0):
    # If we've reached the end of the row, move to the next row
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    # If the current cell is already filled, move to the next cell
    if grid[row][col] != 0:
        return solve(grid, row, col + 1)

    # Try placing numbers from 1 to 9 in the current cell
    for num in range(1, 10):
        if is_move_valid(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True
            grid[row][col] = 0

    return False

# Define the Sudoku grid
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku and print the result
if solve(sudoku_grid):
    for row in sudoku_grid:
        print(" ".join(map(str, row)))
else:
    print("No solution exists for this Sudoku")

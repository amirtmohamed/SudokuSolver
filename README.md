
This script contains a simple Sudoku solver using the backtracking algorithm. The main components of the script are:

1. **is_valid_move(grid, row, col, num)**:
   - This function checks if placing a given number (num) in a specified cell (grid[row][col]) is valid.
   - It ensures that the number is not already present in the current row, column, or 3x3 subgrid.

2. **solve(grid, row=0, col=0)**:
   - This function attempts to solve the Sudoku puzzle using a recursive backtracking approach.
   - It starts from the top-left cell of the grid and progresses through each cell, trying numbers from 1 to 9.
   - If a valid number is found, it places the number in the cell and recursively attempts to solve the rest of the grid.
   - If no valid number can be placed in the cell, it backtracks by resetting the cell to 0 and trying the next number.

3. **sudoku_grid**:
   - This is a 9x9 list representing the Sudoku puzzle to be solved.
   - Zeros in the grid represent empty cells that need to be filled.

4. **Main execution**:
   - The script calls the `solve` function to solve the Sudoku puzzle.
   - If the puzzle is solved, it prints the solved grid.
   - If the puzzle cannot be solved, it prints a message indicating that no solution exists.

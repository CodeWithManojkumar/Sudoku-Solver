grid = [[0, 0, 0, 0, 8, 0, 0, 9, 4],
        [7, 0, 1, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 5, 0, 7, 0, 0],
        [6, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 9, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0]]


def is_valid_move(grid, row, col, number):
    for x in range(9):
        if grid[row][x] == number:
            return False

    for x in range(9):
        if grid[x][col] == number:
            return False

    corner_row = row-row % 3
    corner_col = col-col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row+x][corner_col+y] == number:
                return False
    return True


def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col+1)

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col+1):
                return True

        grid[row][col] = 0
    return False


if (solve(grid, 0, 0)):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("No solution")

'''
Solution:
2 5 6 1 8 7 3 9 4 
7 4 1 3 9 2 8 5 6 
3 8 9 4 6 5 2 7 1 
9 3 4 6 5 1 7 8 2 
6 7 8 2 4 9 5 1 3 
1 2 5 8 7 3 4 6 9 
8 9 2 7 1 4 6 3 5 
5 6 3 9 2 8 1 4 7 
4 1 7 5 3 6 9 2 8 
'''

def main():
    file = open("sudoku.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()
        print(line)


# N is the size of the 2D matrix N*N
N = 9


# A function to print grid
def printing(arr):
    for j in range(N):
        print(arr[j])

# Check to see if it is possible to assign num to the row, and col
def isPossible(board, row, col, num):
    # See if the same num in the same row, return false
    for x in range(9):
        if board[row][x] == num:
            return False

    # See if the same num in the same col, return false
    for x in range(9):
        if board[x][col] == num:
            return False

    # See if the same num is in that 3x3 matrix, return false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True


# Takes a partially filled-in grid and attempts
# to assign values to all unassigned locations in
# such a way to meet the requirements for
# Sudoku solution (non-duplication across rows,
# columns, and boxes) */
def solveSuduko(board, row, col):
    # Check if we have reached the 8th
    # row and 9th column (0
    # indexed matrix) , we are
    # returning true to avoid
    # further backtracking
    if (row == N - 1 and col == N):
        return True

    # Check if column value becomes 9 ,
    # we move to next row and
    # column start from 0
    if col == N:
        row += 1
        col = 0

    # Check if the current position of
    # the grid already contains
    # value >0, we iterate for next column
    if board[row][col] > 0:
        return solveSuduko(board, row, col + 1)
    for num in range(1, N + 1, 1):

        # Check if it is safe to place
        # the num (1-9) in the
        # given row ,col ->we
        # move to next column
        if isPossible(board, row, col, num):

            # Assigning the num in
            # the current (row,col)
            # position of the grid
            # and assuming our assigned
            # num in the position
            # is correct
            board[row][col] = num

            # Checking for next possibility with next
            # column
            if solveSuduko(board, row, col + 1):
                return True

        # Removing the assigned num ,
        # since our assumption
        # was wrong , and we go for
        # next assumption with
        # diff num value
        board[row][col] = 0
    return False


# Driver Code

# 0 means unassigned cells
board = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]

if (solveSuduko(board, 0, 0)):
    printing(board)
else:
    print("no solution exists ")



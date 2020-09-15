# you are working on a logic game made up of a series of puzzles. The first type of puzzle you settle on is "sub-Sudoku", a game where the player has to position the numbers 1...N on an NxN matrix.
# your job is to write a function that, given an NxN matrix, determines if the matrix is valid. A matrix is valid if every row and column contains exactly the numbers 1...N. For example, in a 4x4 matrix, each row and column would contain the numbers 1, 2, 3, and 4.
#if the matrix is valid , return "VALID". If it is not Valid, return "INVALID"
#The matrix may contain any interger, not just 1...N and not just positive. However, the grid will only contain integers.

#example a valid matrix 
#1 2 3
#2 3 1
#3 1 2

def check_sub-sudoku(mat):
     N = len(mat)
     valid_set = set(range(1, N + 1))
     for i in range (N):
         row_set = set()
         col_set = set()
         for j in range (N):
             col_set.add(mat[j][i])
             row_set.add)mat[i][j])
        if col_set != valid_set or row_set != valid_set:
            return "INVALID"
    return "VALID"

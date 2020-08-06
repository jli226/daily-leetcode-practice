# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        for i, j in product(range(m), range(n)):
            #count live neighbors 
            nbr = 0 
            for ii, jj in product(range(i-1, i+2), range(j-1, j+2)):
                if 0 <= ii < m and 0 <= jj < n and (ii != i or jj != j) and board[ii][jj] in (-1, 1): nbr += 1

            if board[i][j] and (nbr < 2 or nbr > 3): board[i][j] = -1 # live to dead (overshoot)
            elif not board[i][j] and nbr == 3: board[i][j] = 2 #dead to live (overshoot)
        
        #recode the table 
        for i, j in product(range(m), range(n)):
            board[i][j] = int(board[i][j] > 0) 
                
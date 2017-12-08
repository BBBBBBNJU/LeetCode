class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def get_live_number(i, j):
            number = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x + i >= 0 and x + i <len(board) and y + j >= 0 and y + j < len(board[0]):
                        if not (x == 0 and y == 0):
                            number += board[x + i][y + j] & 1
            return number
                        
            
        for x in range(len(board)):
            for y in range(len(board[0])):
                # x, y is current position
                live_number = get_live_number(x, y)
                if live_number == 3 or (live_number == 2 and board[x][y] & 1 == 1):
                    board[x][y] |= 2
                
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] >>= 1
        
    

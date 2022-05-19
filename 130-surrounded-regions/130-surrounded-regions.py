class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        border, q = deque(), deque()
        visit = set()
        direcs = [(1,0),(0,1),(0,-1),(-1,0)]
        
        for i in range(len(board[0])):
            if board[0][i] == "O" : border.append((0,i))
            if board[-1][i] == "O": border.append((len(board)-1,i))
        for j in range(1,len(board)-1):
            if board[j][0] == "O" : border.append((j,0))
            if board[j][-1] == "O": border.append((j,len(board[0])-1))
        
        while border:
            (i,j) = border.popleft()
            for r, c in direcs:
                new_r, new_c = i+r, j+c
                if new_r in range(row) and new_c in range(col) and board[new_r][new_c] == "O" and (new_r, new_c) not in visit:
                    visit.add((new_r, new_c))
                    border.append((new_r, new_c))
                    
        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if (i,j) not in visit: board[i][j] = "X"
        
        return board
                    
                    
            
        
        
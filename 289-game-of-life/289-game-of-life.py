class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        m = len(board)
        n = len(board[0])
        
        graph = [[0] * n for i in range(m)]
        
        dx = [-1,0,1,-1,1,-1,0,1]
        dy = [-1,-1,-1,0,0,1,1,1]
        
        for i in range(m) :
            for j in range(n) :
                #이웃수 카운트
                count = 0
                for k in range(len(dx)) :
                    mx = j+dx[k]
                    my = i+dy[k]
                    if mx >= 0 and mx < n and my>=0 and my < m :
                        if board[my][mx] == 1 :
                            count +=1
                if board[i][j] == 0 :
                    if count == 3 :
                        graph[i][j] = 1
                else :
                    if count >= 2 and count <=3 :
                        graph[i][j] = 1
                    else :
                        graph[i][j] = 0
        for i in range(m) :
            for j in range(n) :
                board[i][j] = graph[i][j]
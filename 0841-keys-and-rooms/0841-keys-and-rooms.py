class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]*(len(rooms))
        
        def dfs(now) :
            visited[now] = 1
            for i in rooms[now] :
                if visited[i] == 0 :
                    dfs(i)
        dfs(0)
        
        for check in visited :
            if check == 0 :
                return False
        
        return True
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n+1)]
        visited = [0]*(n+1)
        self.answer = False
        
        for a, b in edges :
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(s, e) :
            if s == destination :
                self.answer = True
                return
            for i in graph[s] :
                if visited[i] == 0 :
                    visited[i] = 1
                    dfs(i, e)
        
        dfs(source, destination)
        
        return self.answer
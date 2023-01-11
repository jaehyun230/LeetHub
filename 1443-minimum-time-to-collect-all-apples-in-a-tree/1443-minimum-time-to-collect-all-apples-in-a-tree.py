class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.res = 0
        adj = {i : [] for i in range(n)}
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
                            
        visited = set()
        def dfs(node):
    
            has = hasApple[node]
            
            if node in visited:
                return False
            
            visited.add(node)
            
            for child in adj[node]:
                decendantHasApple = dfs(child)
                has = has or decendantHasApple
                
            if has and node != 0:
                self.res += 2
            
            return has
        
            
        dfs(0)
        
        return self.res
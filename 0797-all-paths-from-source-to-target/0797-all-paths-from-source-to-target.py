class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        self.answer = []
        
        def dfs(now, path) :
            if now == len(graph)-1 :
                self.answer.append(path)
            else :
                if len(graph[now]) > 0 :
                    for i in graph[now] :
                        dfs(i, path+[i])
            
        dfs(0, [0])
        
        return self.answer
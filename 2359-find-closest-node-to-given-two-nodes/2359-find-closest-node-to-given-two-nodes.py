class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        curr = [(node1,1),(node2,2)] #assuming both nodes are in curr
        visited = [0]*len(edges)
        ans = inf
        while curr:  # level wise BFS
            new = []
            f = False
            for a,w in curr:
                if visited[a]==0:
                    if edges[a]!=-1:
                        new.append((edges[a],w))
                    visited[a] = w
                elif visited[a]!=w: # we find our answer in this condition.no need to run while loop again
                    f = True
                    ans = min(a,ans)        
            if f:
                return ans       
            curr = new # assign next level array-> new to curr
        return -1
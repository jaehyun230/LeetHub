class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        q = deque() 
        dic = {'L': -1, 'R': 1} 
        was = [0 for _ in range(len(dominoes))]
        
        res = list(dominoes)
        # Add to queue nodes with 'L' or 'R' as a sources
        for i, x in enumerate(dominoes): 
            if x != '.':
                q.append((i, 1, x))
                was[i] = -1
		# BFS
        while q: 
            idx, depth, direction = q.popleft()
            if idx < 0 or idx >= len(res): # Check whether the borders are exceeded
                continue
            if was[idx] == depth: # Check if this node is pushed from both sides
                res[idx] = '.'
            elif was[idx] <= 0: # Check if this node haven't been visited
                was[idx] = depth
                q.append((idx + dic[direction], depth + 1, direction))
                res[idx] = direction
                
        return ''.join(res)
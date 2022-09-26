class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = [x for x in range(26)]
        
        def find(a) :
            if parent[a] == a :
                return a
            parent[a] = find(parent[a])
            
            return parent[a]
        
        def union(a, b) :
            p1 = find(ord(a)-ord("a"))
            p2 = find(ord(b)-ord("a"))
            
            if p1 == p2: 
                return
            else: 
                parent[p2] = p1
        
        for equation in equations :
            if equation[1:-1] == "==":
                union(equation[0], equation[-1])
        
        for equation in equations :
            if equation[1:-1] == "!=":
                a, b = ord(equation[0]) - ord('a') , ord(equation[-1]) - ord('a')
                if find(a) == find(b) :
                    return False
            
        return True
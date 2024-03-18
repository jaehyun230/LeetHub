class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        answer = 0
        
        stack = []
        points.sort(reverse=True)
        arrow = points[-1][0]
        
        for point in points :
            if not point[0] <= arrow <= point[1] :
                arrow = point[0]
                answer +=1
        
        if answer == 0 :
            return 1
            
        return answer
    
        
        
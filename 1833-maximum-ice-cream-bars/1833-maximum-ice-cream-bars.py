class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        answer = 0
        for cost in costs :
            if coins -cost >= 0 :
                coins -=cost
                answer +=1
        
        return answer
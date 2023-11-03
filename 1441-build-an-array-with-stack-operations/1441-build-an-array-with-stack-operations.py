class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        temp = []
        result = []
        start = 1
        for i in target :
            for j in range(start, i+1) :
                result.append("Push")
                if j not in target :
                    result.append("Pop")
            
            start = i+1
                
        
        return result
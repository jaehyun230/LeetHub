class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        self.answer = []
        
        
        
        def search(value, target_len) :
            
            if target_len == n :
                self.answer.append(value)
            else :
                for i in range (10) :
                    temp = value%10
                    if temp - i == k :
                        search(value*10+i, target_len+1)
                    elif i - temp == k :
                        search(value*10+i, target_len+1)
        
        for i in range (1, 10) :
            search(i, 1)
        
        return self.answer
                            
                        
                
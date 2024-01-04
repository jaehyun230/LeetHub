class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        counter = []
        for num in bank :
            counter.append(num.count('1'))
        
        answer = 0
        
        start = 0
        for count in counter :
            if count > 0 and start == 0 :
                start = count
            
            elif count > 0 :
                answer +=start * count
                start = count
        
        
        return answer
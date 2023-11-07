class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        
        shot = 0
        time = []
        for i in range(len(dist)) :
            expect_time = float(dist[i]/speed[i])
            time.append(expect_time)
        
        time.sort()
        
        while shot < len(dist) :
            target = time[shot]
            if shot < time[shot] :
                shot +=1
            else :
                return shot
        
        return shot
            
            
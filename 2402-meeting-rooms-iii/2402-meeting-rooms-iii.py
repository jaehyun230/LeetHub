import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        rooms = [0] * (n)
        room_time = [0] * (n)
        q = []
        
        meetings.sort()
        
        for i in range(len(meetings)) :
                
            start, end = meetings[i][0], meetings[i][1]
            
            min_time = room_time[0]
            small_room = 0
            for j in range(n) : 
                if room_time[j] <= start :
                    room_time[j] = start
                    small_room = j
                    break
                elif room_time[j] < min_time :
                    min_time = room_time[j]
                    small_room = j
            
            
            room_time[small_room] += (end-start)
            rooms[small_room] +=1
        
        
        
        answer, counter = 0, 0
        for k in range(n) :
            if rooms[k] > counter :
                counter = rooms[k]
                answer = k
            
        return answer
                
        
        
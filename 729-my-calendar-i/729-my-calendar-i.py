import bisect

class MyCalendar:

    def __init__(self):
        self.cal=[]

    def book(self, start: int, end: int) -> bool:
        
        if self.cal:
            i=bisect.bisect_left(self.cal, [start,end])
            if (i and (self.cal[i-1][1]>start)or
                (i<len(self.cal) and end>self.cal[i][0])):
                return False
            self.cal.insert(i,[start,end])
            return True
        else:
            self.cal.append([start,end])
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
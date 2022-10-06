class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.d:
            self.d[key].append((value, [timestamp, timestamp]))
        else:
            prev_val = self.d[key][-1][0]
            self.d[key][-1][1].pop()
            
            if value == prev_val:
                self.d[key][-1][1].append(timestamp)
            else:
                self.d[key][-1][1].append(timestamp-1)
                self.d[key].append((value, [timestamp, timestamp]))

    def get(self, key: str, timestamp: int) -> str:
        # Time - O(n)
        if key not in self.d:
            return ""
        if self.d[key][-1][1][1] <= timestamp:
            return self.d[key][-1][0]
        for (val, [t0, t1]) in self.d[key][::-1]:
            if t0 <= timestamp <= t1:
                return val
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
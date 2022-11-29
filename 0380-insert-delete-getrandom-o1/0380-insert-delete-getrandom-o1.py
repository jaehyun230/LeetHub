class RandomizedSet:

    def __init__(self):
        self.randSet = defaultdict()

    def insert(self, val: int) -> bool:
        
        if val in self.randSet: return False
        
        self.randSet[val]= None
        return True
        
        
    def remove(self, val: int) -> bool:
        
        if val not in self.randSet: return False
        
        self.randSet.pop(val)
        return True

    
    def getRandom(self) -> int:
        
        return choice(list(self.randSet.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
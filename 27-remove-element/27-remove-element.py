class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        start = 0
        
        while start < count :
            nums.remove(val)
            start +=1
        
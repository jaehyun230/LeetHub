class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subsequences = set()

        for num in nums:
            new_subsequences = set()
            new_subsequences.add((num,))
            for s in subsequences:
                if num >= s[-1]:
                    new_subsequences.add(s + (num,)) # a tuple but not a list, hence can store values in set
            subsequences |= new_subsequences
        return [s for s in subsequences if len(s) > 1] #conversion to list so as to filter out if too short
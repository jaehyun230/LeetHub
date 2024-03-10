class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()
        
        dic = {}
        
        for num in nums1 :
            if num not in dic :
                dic[num] = 1
        
        for num in nums2 :
            if num in dic :
                answer.add(num)
        
        
        return answer
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        left, left2 = 0, 0
        
        while left < len(nums1) and left2 < len(nums2) :
            if nums1[left] == nums2[left2] :
                return nums1[left]
            elif nums1[left] < nums2[left2] :
                left +=1
            elif nums1[left] > nums2[left2] :
                left2 +=1
        
        return -1
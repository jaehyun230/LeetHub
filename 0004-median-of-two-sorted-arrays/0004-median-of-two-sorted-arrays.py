class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = [0] * (len(nums1) + len(nums2))
        idx_nums1 = 0  # Index for nums1
        idx_nums2 = 0  # Index for nums2

        # Merge the arrays while maintaining the sorted order
        for i in range(len(merged_array)):
            if idx_nums2 < len(nums2) and (idx_nums1 == len(nums1) or nums2[idx_nums2] < nums1[idx_nums1]):
                merged_array[i] = nums2[idx_nums2]
                idx_nums2 += 1
            else:
                merged_array[i] = nums1[idx_nums1]
                idx_nums1 += 1

        # Calculate the median of the merged array
        if len(merged_array) % 2 == 1:
            return merged_array[len(merged_array) // 2]
        else:
            return (merged_array[len(merged_array) // 2] + merged_array[len(merged_array) // 2 - 1]) / 2.0
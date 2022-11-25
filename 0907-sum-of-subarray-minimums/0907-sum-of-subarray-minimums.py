class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        right, s = [len(arr) - 1] * len(arr), []
        for i in range(len(arr)):
            while s and arr[i] < arr[s[-1]]:
                right[s.pop()] = i - 1
            s.append(i)        

        # This array stores the left most index 'j' for each 'i'
        # such that arr[j] >= arr[i]. '>=' here to handle duplicate cases.
        left, s = [0] * len(arr), []
        for i in range(len(arr) - 1, -1, -1):
            while s and arr[i] <= arr[s[-1]]:
                left[s.pop()] = i + 1
            s.append(i)

        # Using the left and right span, find the sum.
        # No. of subarrays in which arr[i] is minimum: 
        # = (i - left[i] + 1) * (right[i] - i + 1)
        total = 0
        for i in range(len(arr)):
            total += arr[i] * (i - left[i] + 1) * (right[i] - i + 1)
        
        return total % (10**9 + 7)
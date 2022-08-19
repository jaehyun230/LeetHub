class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        C1, C2, C3 = 0, 0, 0
        pre = nums[0] - 2  # prev < x - 1
        counter = Counter(nums)
        for x in counter:
            if pre != x - 1:
                if C1 or C2:
                    return False
                else:
                    C1, C2, C3 = counter[x], 0, 0
            else:
                if counter[x] < C1 + C2:
                    return False
                else:
                    if counter[x] >= C1 + C2 + C3:
                        C1, C2, C3 = counter[x] - C1 - C2 - C3, C1, C2 + C3
                    else:
                        # C1, C2, C3 = 0, C1, C2+counter[x]-C1-C2
                        C1, C2, C3 = 0, C1, counter[x] - C1
            pre = x
        if C1 or C2:
            return False
        return True
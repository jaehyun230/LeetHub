class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count_one = 0
        total = 0

        for char in s:

            if char == '1':
                count_one = count_one + 1
            else:
                total = total + 1
            total = min(total, count_one)

        return total
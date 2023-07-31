class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        M = 0
        for i in nums:
            if i == 1:
                count += 1
                M = max(count, M)
            else:
                count = 0
        return M

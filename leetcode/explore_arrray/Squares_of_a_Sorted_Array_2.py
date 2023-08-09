class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        result = [None] * len(nums)
        pos = len(nums) - 1
        for i in range(len(nums)):
            if abs(nums[right]) >= abs(nums[left]):
                result[pos] = nums[right] ** 2
                right -= 1
            else:
                result[pos] = nums[left] ** 2
                left += 1
            pos -= 1
        return result

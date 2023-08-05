class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        pos: int = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        return nums

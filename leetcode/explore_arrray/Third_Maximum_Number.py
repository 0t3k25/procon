class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = sorted(list(nums))
        if len(nums) < 3:
            return max(nums)
        nums.pop()
        nums.pop()
        return max(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # prepare pointer
        p1 = 0
        for num in nums:
            if num != nums[p1]:
                p1 += 1
                nums[p1] = num
        return p1 + 1

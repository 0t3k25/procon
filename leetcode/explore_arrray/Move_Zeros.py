class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pos = 0
        # 番号があるものを初めから入れていく
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1

        # 0以外の合計数値pos以降から値を入れていく
        for i in range(pos, len(nums)):
            nums[i] = 0

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 2. 場所のマーキング
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res

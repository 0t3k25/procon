class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) > 0:
            nums2_i = 0
            for i in range(len(nums1)):
                if nums1[i] <= nums2[nums2_i]:
                    nums1.insert(i, nums2[nums2_i])
                    nums2_i += 1
                    nums1.pop()


# まだ途中
# 明日やる

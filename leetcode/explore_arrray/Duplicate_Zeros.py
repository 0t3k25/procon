class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # 0の数を取得
        count_of_zero = arr.count(0)
        if count_of_zero:
            i = 0
            for _ in range(len(arr)):
                if arr[i] == 0:
                    arr.insert(i, 0)
                    i += 1
                i += 1
            for _ in range(count_of_zero):
                arr.pop(-1)

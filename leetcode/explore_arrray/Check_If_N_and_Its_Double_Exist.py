class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        index_map = {v: i for i, v in enumerate(arr)}

        for i, num in enumerate(arr):
            if num * 2 in index_map and i != index_map[num * 2]:
                return True
        return False

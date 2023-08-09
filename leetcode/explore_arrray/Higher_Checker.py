class Solution:
    def heightChecker(self, A: List[int]) -> int:
        miss = 0
        correct_A = sorted(A)
        for i in range(len(A)):
            if correct_A[i] != A[i]:
                miss += 1
        return miss

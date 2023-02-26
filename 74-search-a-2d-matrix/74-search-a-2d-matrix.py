class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if target > m[-1]:
                continue
            else:
                return target in m
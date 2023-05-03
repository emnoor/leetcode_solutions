class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = set(x for row in matrix for x in row)
        return target in nums
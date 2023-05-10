class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ns = []
        
        while matrix:
            ns.extend(matrix.pop(0))
            matrix = list(zip(*matrix))
            matrix.reverse()
        
        return ns
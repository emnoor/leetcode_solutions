class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        
        trig = [[1]]
        
        for i in range(1, numRows):
            prev = trig[i - 1]
            trig.append([1] + [x + y for x, y in zip(prev, prev[1:])] + [1])
        
        return trig
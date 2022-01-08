class Solution:
    def __init__(self):
        self.cache = {}
        
    def uniquePaths(self, m: int, n: int) -> int:
        if (m, n) in self.cache:
            return self.cache[(m, n)]
        
        if m == 1 or n == 1:
            return 1
        
        r = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        self.cache[(m, n)] = r
        return r
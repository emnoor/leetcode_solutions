class Solution:
       
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}
        
        def f(m, n):
            if (m, n) in cache:
                return cache[(m, n)]
            
            if obstacleGrid[m-1][n-1]:
                return 0

            if m == 1 and n == 1:
                cache[(m, n)] = 1
            elif m == 1:
                cache[(m, n)] = f(m, n - 1)
            elif n == 1:
                cache[(m, n)] = f(m - 1, n)
            else:
                cache[(m, n)] = f(m - 1, n) + f(m, n - 1)
            
            return cache[(m, n)]
        
        return f(len(obstacleGrid), len(obstacleGrid[0]))
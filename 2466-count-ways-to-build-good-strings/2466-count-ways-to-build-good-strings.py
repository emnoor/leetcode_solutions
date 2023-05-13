class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        cache = {}
        
        def dfs(length):
            if length > high:
                return 0
            
            if length in cache:
                return cache[length]
            
            r = 0
            if length >= low:
                r = 1
            
            r += dfs(length+zero) + dfs(length+one)
            r %= 1000000007
            cache[length] = r
            return r
        
        return dfs(0)
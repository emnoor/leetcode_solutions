class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        _cache = {}
        
        def acc(i):
            if i in _cache:
                return _cache[i]
            
            if i >= n:
                return 0
            
            r = max(acc(i+2), acc(i+3))
            _cache[i] = r + nums[i]
            return _cache[i]
        
        if n == 0:
            return 0
        elif n == 1:
            return acc(0)
        else:
            return max(acc(0), acc(1))
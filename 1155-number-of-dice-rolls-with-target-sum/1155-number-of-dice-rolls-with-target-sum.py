MAX = 10**9 + 7


class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < 0:
            return 0
        elif n == 1:
            if 1 <= target <= k:
                return 1
            else:
                return 0
        
        if (n, target) in self.cache:
            return self.cache[n, target]
        
        
        r = sum(self.numRollsToTarget(n - 1, k, target - i) for i in range(1, k + 1)) % MAX
        self.cache[n, target] = r
        return r
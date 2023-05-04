class Solution:
    def __init__(self):
        self.cache = {}

    def numSquares(self, n: int) -> int:
        if n <= 1:
            return n

        if n in self.cache:
            return self.cache[n]

        m = 1
        while m * m <= n:
            m += 1

        self.cache[n] = 1 + min(self.numSquares(n - i * i) for i in range(1, m))
        return self.cache[n]
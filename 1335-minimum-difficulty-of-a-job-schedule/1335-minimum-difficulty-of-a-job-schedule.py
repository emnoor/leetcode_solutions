from functools import lru_cache


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        @lru_cache(None)
        def solve(start: int, d: int) -> int:
            if n - start < d:
                return -1

            if d == 1:
                return max(jobDifficulty[start:])

            min_total_diff = float('inf')
            max_diff = -1
            for i in range(start, n):
                if jobDifficulty[i] > max_diff:
                    max_diff = jobDifficulty[i]

                r = solve(i + 1, d - 1)
                if r >= 0 and max_diff + r < min_total_diff:
                    min_total_diff = max_diff + r

            return min_total_diff

        return solve(0, d)

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        ans = -1
        for i, ch in enumerate(s):
            if ch in seen:
                ans = max(ans, i - seen[ch] - 1)
            else:
                seen[ch] = i
        
        return ans
            
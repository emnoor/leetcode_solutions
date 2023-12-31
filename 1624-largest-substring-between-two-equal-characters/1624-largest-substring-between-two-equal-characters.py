class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        for i, ch in enumerate(s):
            d.setdefault(ch, [i, i])
            d[ch][1] = i
        
        return max(b - a - 1 for a, b in d.values())
            
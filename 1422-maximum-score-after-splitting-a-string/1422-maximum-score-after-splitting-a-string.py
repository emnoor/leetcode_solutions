class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = 0
        
        for i, c in enumerate(s):
            if i == 0:
                if c == "0":
                    zeros = 1
            else:
                if c == "1":
                    ones += 1
        
        score = zeros + ones
        for i, c in enumerate(s):
            if i in [0, len(s) - 1]:
                continue
            elif c == "0":
                zeros += 1
            elif c == "1":
                ones -= 1
            if score < zeros + ones:
                score = zeros + ones
        
        return score
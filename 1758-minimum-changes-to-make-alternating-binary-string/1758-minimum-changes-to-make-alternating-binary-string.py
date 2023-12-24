class Solution:
    def minOperations(self, s: str) -> int:
        option1 = ''.join(itertools.islice(itertools.cycle('01'), len(s)))
        option2 = ''.join(itertools.islice(itertools.cycle('10'), len(s)))
        
        ops1 = 0
        ops2 = 0
        for c, c1, c2 in zip(s, option1, option2):
            if c != c1:
                ops1 += 1
            if c != c2:
                ops2 += 1
        
        return min(ops1, ops2)
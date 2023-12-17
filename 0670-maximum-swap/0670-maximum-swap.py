class Solution:
    def maximumSwap(self, num: int) -> int:
        num_s = [int(d) for d in str(num)]
        num_sorted = sorted(num_s, reverse=True)
                
        for (d1, d2) in zip(num_s, num_sorted):
            if d1 != d2:
                break
        else:
            return num
        
        i1 = num_s.index(d1)
        i2 = len(num_s) - 1 - num_s[::-1].index(d2)
        num_s[i1], num_s[i2] = num_s[i2], num_s[i1]
        return int(''.join(str(d) for d in num_s))
                
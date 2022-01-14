TWO_POW_31 = 2 ** 31

class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        n = 0
        i = 0
        
        # ignore leading white-space
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # check sign
        if i < len(s):
            if s[i] == '-':
                negative = True
                i += 1
            elif s[i] == '+':
                i += 1
        
        while i < len(s):
            if not s[i].isdigit():
                break
                
            if n > TWO_POW_31:
                break
            
            n = n * 10 + int(s[i])
            i += 1
        
        if negative:
            n = -n
        
        n = max(n, -TWO_POW_31)
        n = min(n, TWO_POW_31 - 1)
        return n
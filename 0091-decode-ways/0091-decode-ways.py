from functools import lru_cache


@lru_cache
def num_decodings(s: str) -> int:
    if len(s) == 0:
        return 1

    if s[0] == '0':
        return 0

    if len(s) == 1:
        return 1

    if s[0] == '1':
        return num_decodings(s[1:]) + num_decodings(s[2:])
    elif s[0] == '2':
        if s[1] in {'7', '8', '9'}:
            return num_decodings(s[1:])
        else:
            return num_decodings(s[1:]) + num_decodings(s[2:])
    else:
        return num_decodings(s[1:])
        
        
class Solution:
    def numDecodings(self, s: str) -> int:
        return num_decodings(s)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        si = iter(s)
        
        count = 0
        for gg in g:
            try:
                while True:
                    ss = next(si)
                    if ss >= gg:
                        count += 1
                        break
            except StopIteration:
                break
        
        return count
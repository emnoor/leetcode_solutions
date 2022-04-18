class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        if not satisfaction:
            return 0
        
        get_ts = lambda s: sum(i*x for i, x in enumerate(s, 1))
        
        satisfaction.sort()
        ts = get_ts(satisfaction)
        
        while satisfaction:
            satisfaction.pop(0)
            ts_new = get_ts(satisfaction)
            if ts_new < ts:
                break
            ts = ts_new
        
        return ts
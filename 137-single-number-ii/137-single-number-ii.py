class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = {}
        
        for n in nums:
            if n not in mp:
                mp[n] = 0
            
            mp[n] += 1
        
        for k, v in mp.items():
            if v == 1:
                return k
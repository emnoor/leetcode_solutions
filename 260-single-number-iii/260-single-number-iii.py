class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mp = {}
        
        for n in nums:
            if n not in mp:
                mp[n] = 0
            
            mp[n] += 1
            
        return [k for k, v in mp.items() if v == 1]
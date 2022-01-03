class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        for n, count in counts.items():
            if count > len(nums) // 2:
                return n
        return 0
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        rev = nums[::-1]
        
        for i in range(1, n):
            if nums[i - 1] != 0:
                nums[i] *= nums[i - 1]
            if rev[i - 1] != 0:
                rev[i] *= rev[i - 1]
        
        return max(max(nums), max(rev))
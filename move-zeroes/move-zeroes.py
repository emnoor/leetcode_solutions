class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums = []
        
        for n in nums:
            if n:
                new_nums.append(n)
        
        for _ in range(len(nums) - len(new_nums)):
            new_nums.append(0)
        
        for i, n in enumerate(new_nums):
            nums[i] = n
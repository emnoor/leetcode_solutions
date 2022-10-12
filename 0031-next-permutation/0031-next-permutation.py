class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # start from last, find first non-increasing element
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1

        # the list is in descending order, no next permutation
        # choose the first permutation (ascending order)
        if i < 0:
            nums.reverse()
            return

        # start from last, find the first element larger than nums[i]
        j = n - 1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1

        assert j > i, 'this should never happen'

        # swap nums[i] into nums[j]
        nums[i], nums[j] = nums[j], nums[i]

        # reverse nums[i+1...]
        for k in range((n - i - 1) // 2):
            nums[i + 1 + k], nums[n - 1 - k] = nums[n - 1 - k], nums[i + 1 + k]
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for x in nums:
            if x == 0:
                return 0
            elif x < 0:
                product *= -1
        return product
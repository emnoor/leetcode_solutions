class MedianFinder:

    def __init__(self):
        self._nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self._nums, num)

    def findMedian(self) -> float:
        n = len(self._nums)
        if n % 2 != 0:
            return self._nums[n // 2]
        else:
            return (self._nums[(n // 2) - 1] + self._nums[n // 2]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
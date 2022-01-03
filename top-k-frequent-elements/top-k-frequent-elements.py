from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        items = list(counter.items())
        items.sort(reverse=True, key=lambda x: x[1])
        
        return [item for item, _ in items[:k]]
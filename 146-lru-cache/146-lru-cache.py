class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._counter = 0
        self._storage = {}
        self._usage = {}
    
    def _update_usage(self, key: int) -> None:
        self._counter += 1
        self._usage[key] = self._counter

    def get(self, key: int) -> int:
        if key not in self._storage:
            return -1

        self._update_usage(key)
        return self._storage[key]

    def put(self, key: int, value: int) -> None:
        self._update_usage(key)
        self._storage[key] = value
        
        if len(self._storage) > self._capacity:
            lru = min(self._usage.items(), key=lambda x: x[1])[0]
            self._usage.pop(lru)
            self._storage.pop(lru)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
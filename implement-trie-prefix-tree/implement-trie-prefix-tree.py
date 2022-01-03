class Trie:

    def __init__(self):
        self._map = {}

    def insert(self, word: str) -> None:
        _map = self._map
        for c in word:
            if c not in _map:
                _map[c] = {}
            _map = _map[c]
        _map[None] = True   # mark end of word
        # print(f"after insertion of {word=}, {self._map=}")

    def search(self, word: str) -> bool:
        # print(f"before search of {word=}, {self._map=}")
        try:
            _map = self._map
            for c in word:
                _map = _map[c]
            if _map[None]:
                return True
        except KeyError:
            pass
        return False

    def startsWith(self, prefix: str) -> bool:
        # print(f"before startsWith of {prefix=}, {self._map=}")
        try:
            _map = self._map
            for c in prefix:
                _map = _map[c]
            return True
        except KeyError:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
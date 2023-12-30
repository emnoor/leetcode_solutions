from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        
        c = Counter()
        for word in words:
            c.update(word)
        
        for _, count in c.items():
            if count % n != 0:
                return False
        return True
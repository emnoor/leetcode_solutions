def is_palindrome(s: str) -> bool:
    n = len(s)
    for i in range(n):
        if s[i] != s[n-1-i]:
            return False
    return True


class Solution:
    def __init__(self) -> None:
        self.partitions = []
        
    def partition(self, s: str, partition=None) -> List[List[str]]:
        if partition is None:
            partition = []
        
        if s == "":
            self.partitions.append(partition)
            return
        
        for i in range(len(s)):
            if is_palindrome(s[:i+1]):
                self.partition(s[i+1:], partition + [s[:i+1]])
        
        return self.partitions
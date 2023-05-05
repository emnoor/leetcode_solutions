class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vs = 0
        for i in range(k):
            if s[i] in "aeiou":
                vs += 1

        mx = vs
        for i in range(k, len(s)):
            if s[i - k] in "aeiou":
                vs -= 1
            if s[i] in "aeiou":
                vs += 1

            if vs > mx:
                mx = vs

        return mx
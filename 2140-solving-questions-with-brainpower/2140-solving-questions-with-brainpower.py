class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = {}
        n = len(questions)
        
        def f(i):
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            
            # answer this question
            r1 = questions[i][0] + f(1 + i + questions[i][1])
            # skip this question
            r2 = f(i + 1)
            
            r = max(r1, r2)
            cache[i] = r
            return r
        
        return f(0)
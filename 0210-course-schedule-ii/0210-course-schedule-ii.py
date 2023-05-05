from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = {}
        for [a, b] in prerequisites:
            if a not in pre:
                pre[a] = set()
            pre[a].add(b)
        
        # check for cycles in prerequisites
        visited = set()
        
        def contains_cycles(c):
            if c in visited:
                return True
            
            visited.add(c)
            for cc in pre.get(c, []):
                if contains_cycles(cc):
                    return True
            visited.remove(c)
            
            return False
        
        for c in range(numCourses):
            visited.clear()
            if contains_cycles(c):
                return []
        
        order = []
        taken = set()
        
        def take(course):
            if course in taken:
                return
            
            for pre_course in pre.get(course, []):
                take(pre_course)
            
            order.append(course)
            taken.add(course)
        
        for course in range(numCourses):
            take(course)
        
        return order
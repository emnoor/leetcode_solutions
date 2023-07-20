class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroids.reverse()
        stack = [asteroids.pop()]
        
        while asteroids:
            if not stack:
                stack.append(asteroids.pop())
                continue
            
            left = stack.pop()
            right = asteroids.pop()
            
            if not (left > 0 and right < 0):
                stack.append(left)
                stack.append(right)
                continue
                
            if left == -right:
                continue
            elif left > -right:
                stack.append(left)
            else:
                while stack:
                    left = stack.pop()
                    if left < 0:
                        stack.append(left)
                        stack.append(right)
                        break
                    if left == -right:
                        break
                    elif left > -right:
                        stack.append(left)
                        break
                else:
                    stack.append(right)
        
        return stack
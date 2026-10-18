class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for n in asteroids:
            while stack and stack[-1] > 0 and n < 0:
                diff = n + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(n)
        return stack
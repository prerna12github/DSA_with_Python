class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for num in asteroids:
            alive = True
            while stack and stack[-1] > 0 and num < 0: 
                if stack[-1] < abs(num):
                    stack.pop()
                elif stack[-1] == abs(num):
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive == True:
                stack.append(num)

        return stack                        


        
class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = [] 
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1]< -ast:
                    stack.pop()
                    continue
                elif stack[-1]==-ast:
                    stack.pop()
                    break
                elif stack[-1] > -ast:
                    break
            else:
                stack.append(ast)
        return stack

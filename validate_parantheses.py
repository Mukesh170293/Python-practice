from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        if len(s)//2 == 0:
            return False

        for b in s:
            if(b=="{" or b=="(" or b=="["):
                stack.append(b)
            elif (b== "}" and stack[-1] == "{" and len(stack)!=0):
                stack.pop()
            elif(b=="]" and stack[-1] == "[" and len(stack)!=0):
                stack.pop()
            elif(b==")" and stack[-1] == "(" and len(stack)!=0):
                stack.pop()
        if(len(stack)==0):
            return True
        return False

s = Solution()
print(s.isValid("({)}"))
                

class Solution:
    def isPowerOfThree(self,n):
        x = int(n**(1/3))
        cube = x**3
        if(n==cube):
            return True
        return False

s =Solution()
print(s.isPowerOfThree(25))

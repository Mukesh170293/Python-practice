class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        x = 0
        if A != 0:
            return int(A**0.5)
        else:
            return A

s = Solution()
s.sqrt(2)

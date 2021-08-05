class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        for idx in range(0,len(A)):
            if A[idx] == B:
                return idx
        return -1
s = Solution()
print(s.search((4, 5, 6, 7, 0, 1, 2, 3),4))

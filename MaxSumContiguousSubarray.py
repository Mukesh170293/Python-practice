class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_so_far = min(A)
        max_each = 0
        for each in A:
            max_each += each
            if max_each < each:
                max_each = each
            if max_so_far < max_each:
                max_so_far = max_each
        return max_so_far



s = Solution()
print(s.maxSubArray([-20,-150]))

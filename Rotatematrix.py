class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        l = len(A)
        for i in range(0,len(A)):
            for j in range(i,len(A[i])):
                Temp = A[i][j]
                A[i][j] = A[j][i]
                A[j][i] = Temp
        print(A)
        for i in range(0,len(A)):
            temp = A[i][0]
            A[i][0] = A[i][len(A)-1]
            A[i][len(A)-1] = temp
        return A

s = Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))

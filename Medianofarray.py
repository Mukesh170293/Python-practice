class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        c = []
        x = 0
        if (len(A)!=0 and len(B)!=0):
            c = list(A+B)
            c.sort()
        elif(len(A) == 0):
            c.append(B)
        else:
            c.append(A)
        if(len(c)//2 ==0 and c!=[] and len(c)!=1):
            sum = c[len(c)//2]+c[(len(c)//2)+1]
            return float(sum/2)
        elif(len(c)//2 !=0):
            return float(c[(len(c)//2)+1])
        elif(len(c)==1):
            x = c[0]
            return float(x)

s = Solution()
print(s.findMedianSortedArrays((),(20)))

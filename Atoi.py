class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        i = 0
        result = 0
        sign = 1
        flag  = 0
        if (A[0] == "-"):
            sign = -1
            i += 1
        elif (A[0] == "+"):
            sign = 1
            i += 1
        for ch in range(i,len(A)):
            if(A[ch].isdigit()):
                x= int(A[ch])
                flag = 1
            else:
                flag = 0

            if(flag == 1):
                result = result * 10 + (ord(A[ch]) - ord('0'))
                flag = 0
            else:
                break;
        result = result*sign
        return result

s = Solution()
print(s.atoi("-88297 248252140B12 37239U4622733246I218 9 1303 44 A83793H3G2 1674443R591 4368 7 97"))

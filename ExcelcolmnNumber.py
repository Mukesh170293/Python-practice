class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        result = 0
        for each in A:
            result = result*26+(ord(each)-ord("A")+1)
        return result
s = Solution()
print(s.titleToNumber("AA"))
            

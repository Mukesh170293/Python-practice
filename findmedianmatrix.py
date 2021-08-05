class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        Mat = []
        result = 0
        for i in A:
            Mat = Mat + i
        med = sorted(Mat)
        if(len(med)!=1 and len(med)!=0 and len(med)//2==0):
            result = med[(len(med)//2)-1] + med[(len(med)//2)]
            return result/2
        elif(len(med)!=1 and len(med)!=0 and len(med)//2!=0):
            return med[(len(med)//2)]
        elif(len(med)!=1):
            return med[0]



s =Solution()
print(s.findMedian([   [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]   ]))

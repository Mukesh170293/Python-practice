class Solution:
    def maxRotateFunction(self, nums):
        result = []
        output = 0
        if len(nums) <= 1:
            return 0
        for idx in range(len(nums)):
            result.append(self.rotate(nums[-idx:]+nums[:-idx]))
        output = max(result)
        return output

    def rotate(self,list1):
        sum = 0
        for i in range(len(list1)):
            sum += i*list1[i]
        return sum

s = Solution()
print(s.maxRotateFunction([4]))

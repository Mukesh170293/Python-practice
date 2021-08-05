def twoSum(nums,target):
    result = []
    for i in range(0,len(nums)-1):
        if(nums[i]+nums[i+1] == target):
            result.append(i)
            result.append(i+1)
    return result

print(twoSum([1,2,3,4],5))

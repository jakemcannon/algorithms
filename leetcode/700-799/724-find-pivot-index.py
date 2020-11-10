# My nonoptimal solution
def pivotIndex(nums):
	for i in range(len(nums)):
		sum1 = sum(nums[0:i])
		sum2 = sum(nums[i+1:len(nums)])
        
        if sum1 == sum2:
            return i
    
    return -1
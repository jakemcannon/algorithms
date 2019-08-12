# My solution
def findMaxConsecutiveOnes(nums):
    temp_sum = 0
    result  = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            temp_sum += 1
            if temp_sum > result:
                result = temp_sum
        else:
            temp_sum = 0
    return result

# Leetcode solution with max( ) function
def findMaxConsecutiveOnes(nums):
    count = 0
    max_count  = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            result = max(count, max_count)
            count = 0
    return max(count, max_count)


def arrayPariSum(nums):
	# begin by sorting array
	nums.sort()

    result = 0
    for i in range(len(nums)):
        if i % 2 == 0: #skip by two
            result += nums[i]
    
    return result

# cleaning up % logic
def arrayPariSum(nums):
	# begin by sorting array
	nums.sort()

    result = 0
    for i in range(0, len(nums), 2):
    	result += nums[i]
    
    return result

# even simpler solution
def arrayPariSum(nums):
	# begin by sorting array
	nums.sort()
    return sum(nums[::2])
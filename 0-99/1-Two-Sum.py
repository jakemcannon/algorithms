
def twoSum(self, nums: List[int], target: int) -> List[int]:
	if len(nums) <= 1:
		return False
	aux_dict = {}
	for i in range(len(nums)):
		if nums[i] in aux_dict:
			return [aux_dict[nums[i]], i]
		else: #This is where the entries into the dictonary are actually being made
			aux_dict[target - nums[i]] = i

# Example
#
#[2, 7, 11, 15], target = 9
#

# STEP 1:
# -------------------

# {}
# i = 0
# is 2 in {} ?  -FALSE

# else:
# 	aux_dict[7] = 0
# 	{7:0}

# STEP 2:
# -------------------
# {7:0}
# i = 1
# is 7 in {} ? - TRUE
# 	return [aux_dict[nums[1]], 1]
# 			aux_dict[7] = 0
# 			[0, 1]
#
# -------------------
# This is notation for adding to a Python dictionary
#aux_dict[target - nums[i]] = i
#
# OR aux_dict[KEY] = VALUE

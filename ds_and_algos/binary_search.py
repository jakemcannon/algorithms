

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10

# My incorrect implementation 
# def binary_search(nums, target):
# 	low = 0
# 	high = len(nums) -1
# 	mid = (low+high) / 2

# 	while low < high:
# 		if nums[mid] == target:
# 			return mid
# 		elif mid < target:
# 			low = mid
# 			mid = (low + high) / 2
# 		else:
# 			high = mid
# 			mid = (low + high) / 2
# print(binary_search(nums, target))


def binary_search(nums, target):
	low = 0
	high = len(nums) -1

	while low <= high:
		mid = (low+high) / 2
		if nums[mid] == target:
			return mid
		elif mid < target:
			low = mid +1
		else:
			high = mid -1
	return -1
print(binary_search(nums, target))

# currently not working for index out of range
def recursive_binary_solution(nums, target):
	low = 0
	high = len(nums) -1
	mid = (low + high) // 2

	# recursion while or for?
	if (target == nums[mid]):
		return mid
	elif (target > nums[mid]):
		return recursive_binary_solution(nums[mid+1:], target)
	else:
		return recursive_binary_solution(nums[:mid-1], target)
print(recursive_binary_solution(nums, target))













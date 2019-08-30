# My first solution
# O(n), O(n)
def rotate(nums, k):
	result = []
	index = len(nums) - k
	for i in range(len(nums)):
		# index += 1
		if index >= len(nums):
			index = 0
		result.append(nums[index])
		index += 1
	return result
print(rotate(nums, k))

# Better Solution
# O(n), O(1)
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    self.reverse(nums, 0, len(nums)-1)
    self.reverse(nums, 0, k-1)
    self.reverse(nums, k, len(nums)-1)  
        
def reverse(self, nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
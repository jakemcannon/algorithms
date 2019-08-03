def sortedSquares(nums):
	result = []
        l, r = 0, len(nums) -1
        
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                result.append(left*left)
                l += 1
            else:
                result.append(right*right)
                r -= 1
        result.reverse()
        return result
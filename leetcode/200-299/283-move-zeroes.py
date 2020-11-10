

def moveZeroes(nums):
    lag = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if lag < i:
                nums[lag], nums[i] = nums[i], nums[lag]
            lag += 1
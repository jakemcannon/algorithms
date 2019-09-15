#My nonoptimal solution
def productExceptSelf(self, nums: List[int]) -> List[int]:    
    result = []
    
    # Build freq table
    f = {}
    for i in range(len(nums)):
        f[i] = nums[i]
        
    for i in range(len(nums)):
        product = 1
        for key,value in f.items():
            if key != i:
                product *= value
        result.append(product)
    return result
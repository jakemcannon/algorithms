# My solution
# This is the same as the first Array problem in EPI
def sortArrayByParity(A):

    left, right = 0, len(nums) -1
    while left < right:
        if A[left] % 2 != 0:
            A[left], A[right] = A[right], A[left]
            right -= 1
        else:
            left += 1
    return A


# my solution
def smallest_subarray_with_given_sum(s, arr):
	result = float("inf")
	start = 0
	cur_sum = 0

	for i in range(len(arr)):
		cur_sum += arr[i]

		while cur_sum >= s:
			result = min((i-start)+1, result)
			cur_sum -= arr[start]
			start += 1

	return result

print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
print(" ")

# book solution
def smallest_subarray_with_given_sum(s, arr):
  window_sum = 0
  min_length = float("inf")
  window_start = 0

  for window_end in range(0, len(arr)):
    window_sum += arr[window_end]  # add the next element
    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
    while window_sum >= s:
      min_length = min(min_length, window_end - window_start + 1)
      window_sum -= arr[window_start]
      window_start += 1
  if min_length == float("inf"):
    return 0
  return min_length


print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
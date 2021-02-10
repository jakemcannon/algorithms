def longest_substring_with_k_distinct(str1, k):
	start = 0
	result = 0
	d = {}

	for i in range(len(str1)):
		if str1[i] not in d:
			d[str1[i]] = 1
		else:
			d[str1[i]] +=1

		while len(d) > k:
			d[str1[start]] -= 1
			if d[str1[start]] == 0:
				del d[str1[start]]
			start+=1
		result = max(result, i-start+1)
	return result

print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


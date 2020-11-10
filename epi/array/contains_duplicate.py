# nums = [1, 2, 3, 1]


# d = {}

# for i in nums:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1

# print(d)



nums = [7, 1, 3, 4]

mini = nums[0]
print(mini)
maxi = 0

for num in nums:
	if num < mini:
		mini = num
	else:
		print(maxi)
		maxi = max(maxi, num - mini)

print(maxi)
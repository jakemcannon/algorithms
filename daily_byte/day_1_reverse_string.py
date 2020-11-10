
s1 = "Cat"
s2 = "The Daily Byte"
s3 = "civic"


def reverse_string(s):
	
	result = ""
	for c in s[::-1]:
		result += c

	return result


print(reverse_string(s1))
print(reverse_string(s2))
print(reverse_string(s3))
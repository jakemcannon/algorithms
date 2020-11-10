from collections import Counter

def compress(s):
	toReturn = ""
	temp = s[0]
	count = 0

	for i in s:
		if i == temp:
			if count != 0:
				count += 1
				toReturn = toReturn[:-2] + temp + str(count)
				# print (toReturn)
			else: #edge case for i = 0, first itteration
				count +=1
				toReturn = temp + str(count)

		else: #when we encouter a new char or char sequence
			temp = i
			count = 1
			toReturn += temp + str(count)

	return toReturn

s1 = "aabcccccaaa"
print(compress(s1))

# Basically my approach was to always add the char, i.e. 'a', and the current coun, i.e. 'a2'
# and then overwrite that if there was a duplicate char.
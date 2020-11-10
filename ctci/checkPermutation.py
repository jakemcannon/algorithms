
from collections import Counter

s1 = "abcdbjb"
s2 = "acjdbbb"


def check_permutation(s1, s2):
	if len(s1) != len(s2):
		return False

	d = create_dict(s1)

	# comparing chars of string2 with the keys in dict
	# also subtracting value of dict everytime a common string is encountered
	for c in s2: #O(n)
		if c not in d.keys():
			return False
		else:
			d[c] -= 1

	#initially made a small error here, incorrect syntax for accessing values
	for key, val in d.items(): #O(n)
		print(val)
		if val != 0:
			return False
	return True


def create_dict(string):
	d = {}
	for c in string:
		if c not in d.keys():
			d[c] = 1
		else:
			d[c] += 1
	return d


#Test counter
def test_counter(s1, s2):

	counter = Counter()
	for c in s1:
		print(counter)
		counter[c] +=1
	return counter

# print(test_counter(s1, s2))

#Book solution
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter() #This already initiates everything to 1 so you can skip that if/else block
    for c in str1:
        counter[c] += 1
    #Ok, here, basically everything will get set to 0
    #But we only do 1 iteration of it so 
    for c in str2:
    	print(counter)
    	if counter[c] == 0:
    		return False
    	counter[c] -= 1
    return True

print(check_permutation(s1, s2))


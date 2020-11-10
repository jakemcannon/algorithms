
s = "aab"

def isUnique(string):
	d = {}
	for c in string:
		if c not in d.keys():
			d[c] = 1
		else:
			return False
	return True

print(isUnique(s))
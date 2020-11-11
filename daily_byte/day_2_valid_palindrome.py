# import string

s1 = "Level"
s2 = "algorithm"
s3 = "A man, a plan, a canal: Panama."


def valid_palindrome(s):

	s = s.lower()
	s = s.replace(" ", "")

	start = 0
	end = len(s) - 1

	# NOT WASTING TIME ON PUNCTUATION 
	# for punc in string.punctuation:
	# 	s.replace(punc, "")
	# 	if punc in s:
	# 		s.replace(punc, "")
	# s = s.replace(string.punctuation, "")

	while start <= end:

		if s[start] != s[end]:
			return False

		start +=1
		end -=1

	return True

print(valid_palindrome(s1))
print(valid_palindrome(s2))
print(valid_palindrome(s3))
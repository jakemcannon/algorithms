# COUNTER SOLUTION
# O(N+M) time
# O(N+M) space
ransomNote = collections.Counter(ransomNote) #O(N)
magazine = collections.Counter(magazine) #O(M)
for key, value in ransomNote.items(): #O(1) in Python3
    if value > magazine[key]:
        return False
return True

# Set and .count( ) SOLUTION
# O(N+M) time
# O(N) space
r_Note = set(ransomNote) #O(N) time
for note in r_Note: #O(1) time -> just like a dict "in" os O(1)
    if ransomNote.count(note) > magazine.count(note): #O(N+M) time
        return False
return True

# MY SOLUTION
# O(N+M) time
# O(N) space
d= {}
for char in magazine: #O(N)
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1

for char in ransomNote: #O(M)
    if char not in d or d[char] =< 0:
        return False
    d[char] -= 1
return True

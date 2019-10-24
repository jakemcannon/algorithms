s1 = "[)"
s2 = "[["
s3 = "[([](([]))[])]"

def isValid(s):
    opening = {'[', '{', '('}
    closing = {']', '}', ')'}
    mapping = {'{':'}', '[':']', '(':')'}
    
    if len(s)%2 != 0:
        return False
    
    st = []
    for c in s:
        if c in opening:
            st.append(c)
        elif not st or mapping[st.pop()] != c:
            return False
    if st:
        return False
    return True

# Cleaner
def isValid2(s):
    mapping = {'{':'}', '[':']', '(':')'}
    
    if len(s)%2 != 0:
        return False

    st = []
    for c in s:
        if c in mapping.keys():
            st.append(c)
        elif not st or mapping[st.pop()] != c:
            return False
    return not st

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))

print(" ")

print(isValid2(s1))
print(isValid2(s2))
print(isValid2(s3))



# SOLUTION 1 (Vertical scanning)
def longestCommonPrefix(self, strs: List[str]) -> str:
    #step 1: error check for emmpy list
    if not strs:
        return ""
    
    #test everything on the shortest string
    shortest_str = min(strs, key=len) # O(n)
    lcp = ""
    
    index = 0
    #use the shortest_str as the outer loop
    for c in shortest_str:
        # use != instead of == otherwise...
        # you will catch some unwanted similar chars
        for string in strs:
            # this still checks shortest_str which isn't necessary
            if string[index] != c:
                return lcp
        # Since we havn't hit a falsy char, keep building
        # The != is what breaks us out on first false # condition
        lcp += c
        index += 1
    
    return lcp
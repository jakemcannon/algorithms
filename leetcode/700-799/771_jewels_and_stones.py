def numJewelsInStones(self, J: str, S: str) -> int:
        
    result = 0
    d = {}
    for stone in S:
        if stone not in d:
            d[stone] = 1
        else:
            d[stone] += 1
    
    for jewel in J:
        if jewel not in d:
            continue
        else:
            result += d[jewel]
    return result
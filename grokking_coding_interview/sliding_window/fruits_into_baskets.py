def fruits_into_baskets(fruits):
  result = 0
  start = 0
  d = {}

  for i in range(len(fruits)):
    if fruits[i] not in d:
      d[fruits[i]] = 1
    else:
      d[fruits[i]] += 1

    while len(d) >= 3:
      d[fruits[start]] -=1
      if d[fruits[start]] == 0:
        del d[fruits[start]]
      start += 1
    result = max(result, i - start + 1)
  return result

print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))

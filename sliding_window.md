# Sliding Window

### Hints / giveaways

- Max or min "subarray" , "substring"
- Sliding window
- With "k replacement"
- Contiguous, consecutive
  - Sorting can't be used, order matters



### Types of problems / variations

- fixed k sized window
- non-fixed size window
- freq map used for growing and shrinking window
- map used for recording indices ?
- Finding pattern, permutation, in string



### Boiler plate code

- Create a `min` or `max` result variable and initially set to `-infinity` or `infinity`
- Use a for loop as the `window_end` pointer
- Add to dict with `window_end` or reduce with `window_start`
- Typically take `min()` or `max()` at the end of every iteration
- `window_end - window_start + 1` will give you the length of your window



### Basics (fixed length window)

- Average contiguous subarrays -> **Just create window of size k**
- Maximum sum subbarray of size k



### Non-fixed sized window

- Minimum sized subarray sum -> **While loop to shrink whindow while current sum window >= target**



### Dictionary used to shrink

- Longest Substring with At Most K Distinct Characters -> **Use dict to maintain char freq within window, if dict length exceeds k then shrink window** without dict space solution??

- Fruit into baskets -> **Use dict to maintain char freq, if dict length > 2 (basket size), shrink window**
- Longest substring with at most two distinct characters -> **Use dict to maintain char freq, if dict length > 2, shrink window**
- Longest substring with at most k distinct characters -> **Use dict to maintain char freq, if dict length > k, shrink window**

-  Longest Repeating Character Replacement -> **Keep track of longest_substring, use formula: window_end - window_start +1 - longest_substring**

- Max consecutive ones II -> **Create counter variable to keep track of zeros seen, if counter > 1 then shrink window **
- Max consecutive ones III -> **Create counter variable to keep track of zeros seen, if counter > k then shrink window**



*these three problems use a dictionary and match_counter pattern*

- Permutation in string ->
- Find all anagrams in a string ->
- Minimum window substring ->

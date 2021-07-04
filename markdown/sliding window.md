### LC 209. Minimum Size Subarray Sum
* left and right pointers
* when target met, shrink the window by increment left pointer


### LC 424. Longest Repeating Character Replacement
* two pointers, left and right, and use a map to record every character's frequency in use(Replacement), and a max frequency record
* for every character, update the character frequency and the max frequency
* if the max frequency + k is larger than the current window, increment left and update the left character frequency
* return the window size


### LC 978. Longest Turbulent Subarray
* to find out the longest subarray with flip comparison signs
* init left index = 0, longest = 1
* do a for loop with variable right from (1, n)
* comparison sign = Integer.compare(arr[right - 1], arr[right])
* if sign = 0, move left to right
* if right at the end or the comparison sign is the same with arr[right] and arr[right + 1], update longest
### LC 1004. Max Consecutive Ones III
* two pointers, left and right
* if encounter zero, decrement k by one, if k is less than zero, start moving left, k += right == 0
* update longest

### LC 1658. Minimum Operations to Reduce X to Zero
* reverse thinking: find the max length sub array that has sum equal to array sum - x
* use standard two pointer approach
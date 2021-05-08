### LC 209. Minimum Size Subarray Sum
* left and right pointers
* when target met, shrink the window by increment left pointer


### LC 424. Longest Repeating Character Replacement
* two pointers, left and right, and use a map to record every character's frequency in use(Replacement), and a max frequency record
* for every character, update the character frequency and the max frequency
* if the max frequency + k is larger than the current window, increment left and update the left character frequency
* return the window size


### LC 1004. Max Consecutive Ones III
* two pointers, left and right
* if encounter zero, decrement k by one, if k is less than zero, increment left until k is 0
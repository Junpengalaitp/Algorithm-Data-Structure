## Backtracking
### LC 79. Word Search
* base case: if word length is 1 it's equal to current cell, return true. If current cell is not equal to the start char, return false
* backtracking is a boolean function. On backtracking, sign the current cell to '#', and backtrack the word substring from index 1, if the result is true, return true and end backtrack, else restore current cell to word start char at end. 

### LC 78. Subsets
* backtrack target path sizes is [0, input length]
* on backtrack, start idx becomes current idx + 1

### LC 90. Subsets II
* sort the input array
* backtrack target path sizes is [0, input length]
* on backtrack, skip those numbers that are the same with the previous one and not the starting num in the backtrack loop

## Recursion only
### LC 17. Letter Combinations of a Phone Number 
* init a number to chars map
* the candidates are the chars in digit, path start with empty string
* end condition: finish visiting all the candidates
* recursively call on every char of num, add char to path and visit the next candidate
  
### LC 22. Generate Parentheses
* keep left and right count in backtrack function 
* end condition: path length is 2 * n
* two forks in backtracking
  * if left count is less than n, backtrack path + '(' and increment left by 1
  * if right count is less than left, backtrack path + ')' and increment right by 1

### LC 139. Word Break
* recursion and memorization
* the idea is to enumerate all substrings and if current substring is valid, recursively call on the remaining substrings
* base case: if current start index is the end of the string, return true.
* loop all substrings start from this index, if current substring is valid and recursion on remaining substring returned true, return true
* if not return true, return false at end
* use a cache to cache result



### 611. Valid Triangle Number
* backtrack
* sort the input, so we can filter out the edges that are already larger than current 2 edges sum

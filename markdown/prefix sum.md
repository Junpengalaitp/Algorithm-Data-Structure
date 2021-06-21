### LC 560. Subarray Sum Equals K
* init a sum and a count variables, start with 0
* use a map to record current sum count, init with value <0, 1>(sum 0 has 1 way)
* for every value from the array, add it to the sum, and increment the count variable by the sum - k in map(default 0)

### LC 1248. Count Number of Nice Subarrays
* use a pre variable to record odd number occurrence up to nums[i];
* if pre >= k, add count[pre - k] to res
* count[pre]++ for each num

### LC 1371. Find the Longest Substring Containing Vowels in Even Counts
* use xor to count prefix sum
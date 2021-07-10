### LC 467. Unique Substrings in Wraparound String
* count max length continuous(diff == 1 or -25) subarray up to current char, the max is the max of prefix sum and current counter
* prefix sum: if (diff == 1 or -25), increment, else reset to 1
* return the sum of counter

### LC 560. Subarray Sum Equals K
* use a map to put prefix sum for every number, and init value 0 -> 1
* because later we check prefix sum - k result is in map or not, if prefix sum - k == 0, there is one match.
* check prefix sum - k for every number, if the result in counter map, add map value count.
* increment prefix sum value in counter map by 1

### LC 795. Number of Subarrays with Bounded Maximum
* do two sub arrays sum not greater than target, which are left - 1 and right bound
* the result is prefixSum(right) - prefixSum(left - 1)
### LC 848. Shifting Letters
* convert the shifts array to reverted prefix sum array
* in the conversion, mod the number by 26
* convert the string by the prefix sum array

### LC 1094. Car Pooling
* basically same as LC 1109

### LC 1109. Corporate Flight Bookings
* use prefix sum to eliminate the inner loop
* add booking[0] - 1 to res (every number after this index will add this number) 
* subtract booking[1] to res (because at the step above, number not in [booking[0], booking[1]] are incremented by booking[0])
* loop the res array from(1, n), every number += res[i-1], and return res

### LC 1248. Count Number of Nice Subarrays
* prefix sum: number of odd numbers up to current num
* use a map to put prefix sum for every number, and init value 0 -> 1
* because later we check prefix sum - k result is in map or not, if prefix sum - k == 0, there is one match.
* if prefix sum - k > 0, add counter value of prefix - k to count

### LC 1371. Find the Longest Substring Containing Vowels in Even Counts
* use xor to count prefix sum

### LC 1508. Range Sum of Sorted Subarray Sums
* prefix sum on prefix sum


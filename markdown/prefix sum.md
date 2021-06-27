### LC 560. Subarray Sum Equals K
* use a map to put prefix sum for every number, and init value 0 -> 1
* because later we check prefix sum - k result is in map or not, if prefix sum - k == 0, there is one match.
* check prefix sum - k for every number, if the result in counter map, add map value count.
* increment prefix sum value in counter map by 1

### LC 848. Shifting Letters
* convert the shifts array to reverted prefix sum array
* in the conversion, mod the number by 26
* convert the string by the prefix sum array
### LC 1248. Count Number of Nice Subarrays
* prefix sum: number of odd numbers up to current num
* use a map to put prefix sum for every number, and init value 0 -> 1
* because later we check prefix sum - k result is in map or not, if prefix sum - k == 0, there is one match.
* if prefix sum - k > 0, add counter value of prefix - k to count

### LC 1371. Find the Longest Substring Containing Vowels in Even Counts
* use xor to count prefix sum

### LC 1508. Range Sum of Sorted Subarray Sums
* prefix sum on prefix sum
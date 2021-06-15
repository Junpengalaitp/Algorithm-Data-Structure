# Reverse Thinking
## Sub Array
### LC 53. Maximum Subarray
* init max value with the first value in the array 
* for each value from index 1 to the end, the max sum ending at current value is max of current value and current value plus max value of index - 1
* can use a variable to record previous max, so no extra space

### LC 152 Maximum Product Subarray
* init 3 variables, max value, max positive product and min negative product with the first value in the array 
* for each value from index 1 to the end, if the current value is negative, swap the max positive product and min negative product
* update max positive product to the max of itself and current value * itself
* update min negative product to the min of itself and current value * itself
* the max value result is the max of and max positive product

## Subsequence
### LC 300. Longest increasing subsequence
* dp approach
  * init a dp table(1D array) with the size of the array and with values 1
  * for each element in array[1:], search all element before it, if the num before is less than it, the dp[i] = max(dp[i], dp[j] + 1)
  * O(n^2) time and O(n) space
* patience sort(binary search)
  * init a empty list as the best increasing subsequence list
  * for each num in the array, if the num is larger than the last element in the list(or the list is empty), add it to the tail of the list
  * else use binary search to replace an element in the list
  * the result is the list size
  * O(nlogn) time and O(n) space

### LC 115. Distinct Subsequences
* use a 2D dp table
* two choices, match s[i+1] and t[j+1] or [s+1] and t[j]
* if s[i] != t[j], can only match s[i + 1] and t[j]
* if s[i] == t[j], can match both
### LC 5. Longest Palindromic Substring
* use a 2D matrix as dp table, init with all boolean true values, and process it from right bottom to top left
* each row and col index represents substring from row to col + 1
* if the char at row and the char at col is not equal, then it's cannot be a palindrome, put false in matrix
* if they are equal, it has the possibility to be a palindrome, we further check the substring from row + 1, col - 1 is palindrome or not, which is already exist in the dp table
* if the current substring is a palindrome and the length is longer than the current longest, update the current longest with the current substring

### LC 55. Jump Game
* dynamic programming
  * the last position is reachable
  * iterate backwards, each index loop to the farthest to see if any are reachable
  * time complexity O(n^2), space complexity O(1) (can reuse the input array)
* greedy
  * init a reachable index, start with the last index
  * iterate backwards, each index check its value + index is greater than or equal to the reachable index, if it is, update reachable index to current index
  * return the reachable index is 0
### LC 120. Triangle
* recursive
  * base case: if level equals triangle size, return 0
  * recursive calling level + 1 and add min of current index and index + 1 to current value
  * use a cache
  * O(n) time and space, n = total values
* iterative
  * start from level 1(the second level)
  * update values of each level are the value plus min of upper level col - 1 and col (need to deal with index out of bound)
  * the min of the last row is the answer
  * can reuse the triangle itself, no extra space
  * O(n) time, n = total nodes

### LC 91. Decode Ways
* base case 1: if the string is empty, return 1
* base case 2: if the string starts with 0, return 0
* decode 1: recurse on substring(1)
* decode 2: recurse on substring(2) if the number is larger than 26, else is 0
* total ways = decode 1 + decode 2
* use cache to reduce duplicated calculation

## State Machine
### Stock problem
* 3 options each day: buy, sell and reset
* state transfer
  * 0(holding no stock), 1(holding a stock)
  * 0 can result from selling a stock(1 -> 0) or do noting(reset) when holding no stock(0 -> 0)
  * 1 can result from buying a stock(0 -> 1) or do noting(reset) when holding a stock(1 -> 1)
* dp table
  * dp[i][k][0]: state which is holding no stock at day i with max K transactions, equals to max of reset(dp[i-1][k][0]) or selling (prices[i] + dp[i-1][k][1])
  * dp[i][k][1]: state which is holding a stock at day i with max K transactions, equals to max of reset(dp[i-1][k][1]) or buying (dp[i-1][k-1][0] - prices[i])
  * base cases
    * dp[-1][k][0] = 0, before start, no action can be taken
    * dp[-1][k][1] = 0, before start, no action can be taken
    * dp[i][0][0] = 0, with no transaction permit, no action can be taken
    * dp[i][0][1] = 0, with no transaction permit, no action can be taken

### LC 121. Best Time to Buy and Sell Stock
* can take only one transaction, so k = 1
  * dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
  * dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i]) = max(dp[i-1][1][1], -prices[i]) (k = 0 is a base case)
* all k in formula are 1, so we can eliminate k
  * dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
  * dp[i][1] = max(dp[i-1][1], -prices[i])  
* do not need a dp table, just two variables for recording, O(n) time and O(1) space

### LC 122. Best Time to Buy and Sell Stock II
* can take any amount of transactions, k = inf, which can mean k = k - 1
  * dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
  * dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]) = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
* k in not going to change in formula, so we can eliminate k
  * dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
  * dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
* just need one extra variable to store dp[i-1][0], O(n) time and O(1) space 

### LC 309 Best Time to Buy and Sell Stock with Cooldown
* same with LC 122, just change the holding state result from buying from i - 1 to i - 2
  * dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
  * dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

### LC 714 Best Time to Buy and Sell Stock with Transaction Fee
* same with LC 122, just subtract fee from selling price
  * dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
  * dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i] - fee)

### LC 123 Best Time to Buy and Sell Stock III
* k = 2, can not simplify formula using k
  * dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
  * dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
* have to do a loop regrading to k, and dp[0][k][1] = -prices[0]

### LC 188. Best Time to Buy and Sell Stock IV
* k = any, but if k > n/2(n = days), the k is meaning less, which we can solve it as LC 122
* else we can solve it the same way with LC 123

### 0/1 knapsack
### LC 416. Partition Equal Subset Sum
* Basically this question is asking us are they any combinations that has the target sum(total sum / 2), so it's a 0/1 knapsack problem
* O(mn) time and space
  * use a 2D dp table, rows are nums length + 1, cols are target sum + 1
  * first index of each col init to true, because if the target is 0, we can choose nothing to fulfill this target, no matter what the options are
  * iterate from row 1 and col 1, if the upper row with the same col is true, the current cell is true
  * else we subtract the current num from col(col is te current  target sum), if the upper row with updated col is true, the current cell is true
  * return the last row and col as answer
* O(mn) time, O(n) space
  * because we only care about the previous row, so 1D dp table is enough
  * have to iterative backwards or use a temp array
  
### Array
### LC 746. Min Cost Climbing Stairs
* init a dp array with the input length, and dp[0] = costs[0], dp[1] = costs[1]
* start from index 2, dp[i] = costs[i] + Math.min(dp[i - 1], dp[i-2]])
* return min of dp[n - 1] and dp[n - 2]

## Matrix
### LC 221. Maximal Square
* max side length min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
* return max side length squared

## Other
### LC 279. Perfect Squares
* init an array with squares from 0 to sqrt(n) + 1
* init a dp array from 0 to n + 1 with value inf except the first one which is 0 (base case)
* for every number from 1 to n, loop the squares array, dp[i] = min(dp[i], dp[i - squares[j]] + 1)

### LC 322. Coin Change
#### iterative
* init a dp array with length amount + 1, and fill it with amount + 1 (cannot use Integer.MAX_VALUE, it could overflow), and dp[0] = 0
* loop the dp array and coin array, dp[i] = min(dp[i], dp(i - coin))
* return dp[-1] if dp[-1] != amount + 1 else -1

#### recursive
* use a cache, base case 1: return -1 if amount < 0, base case 2: return 0 if amount == 0
* init min with Integer.MAX_VALUE, loop the coin array, recurse on amount - coin and update the min with result + 1 if result >= 0 and result < min
* return min if min != amount + 1 else -1


### LC 198. House Robber
* init a dp array with nums length.
* base cases: dp[0] = nums[0], dp[1] = nums[1], dp[2] = max(dp[1], dp[0] + dp[2])
* loop form 3 to the nums length, dp[i] = max(dp[i - 2] + nums[i], dp[i - 3] + nums[i])
* can reuse nums array as dp array to reduce space

### LC 213. House Robber II
* the max of rob (nums[1:] and nums[:-1])

### LC 337. House Robber III
* the helper function return two results: rob current and do not rob current
* rob current = node.val + helper left no rob + helper right no rob
* no rob = max(left rob, left no rob) + max(right rob, right no rob)

### LC 343. Integer Break
* dp recursion, the sub problem is to get max of (n - i) * i and dp(n - i) * i

### LC 494. Target Sum
* backtracking and memorization.
* base case: the index is at the end of input list, return 1 or 0 (sum equals or not equals target).
* backtrack on current sum plus and minus current index number.
* use a 2D cache to cache current index and result(plus + minus)

### LC 5. Longest Palindromic Substring
* 2D dp boolean table, dp[row][col] represent substring s[row:col+1] is palindromic or not
* dp[row][col] = true if s[row] == s[col] and s[row, col+1] length less or equal to 3, it's palindromic('a', 'aa', 'aba'(length 3 is palindrome regardless the mid char)
* dp[row][col] = true if s[row] == s[col] and s[row + 1: col - 1](the mid substring is palindromic)
* if dp[row][col] == true, update the longest variable

### LC 516. Longest Palindromic Subsequence
* 2D int dp table, dp[row][col] the longest palindromic subsequence represents substring s[col:row+1]
* int dp table with value 0 and diagonal value with the value 1
* dp[row][col] = dp[row+1][col-1] + 2 if s[row] == s[col]
* dp[row][col] = max(dp[row][col-1], dp[row+1][col]) is s[row] != s[col]

### LC 518. Coin Change 2
* can use backtracking, but time will exceed the limit
* use dynamic programming, dp[i][j] represent how many ways for amount i use coins up to j
* base case: for amount 0, there is one way to make it: choose no coin
* can use 1D dp table to reduce space

### LC 560. Subarray Sum Equals K
* init a sum and a count variables, start with 0
* use a map to record current sum count, init with value <0, 1>(sum 0 has 1 way)
* for every value from the array, add it to the sum, and increment the count variable by the sum - k in map(default 0)

### LC 673. Number of Longest Increasing Subsequence
* same with LC 300, but need an extra dp array for counting
* if dp[j] < dp[i], before change the dp[i], compare current length of dp[i] and dp[j]
* if dp[j] >= dp[i], longestCount[i] = longestCount[j]
* if dp[j] == dp[i] - 1, longestCount[i] += longestCount[j]
* at the end, longest count is the sum of the longestCount[i] that dp[i] == longest

### LC 718. Maximum Length of Repeated Subarray
* init a 2D dp table with rows = len(nums2) + 1 and cols = len(nums2) + 1
* if nums[row-1] == nums[col-1], dp[row][col] = dp[row-1][col-1] + 1

### LC 118. Pascal's Triangle, 119. Pascal's Triangle II
* every row reuse the prev row res

### LC 935. Knight Dialer
* init a static map to record possible end point from 0-9
* recursive dp, base case: return 1 if n == 1
* recursively call on next end point and n - 1
* use a cache, and BigDecimal for dp return value type

### LC 1031. Maximum Sum of Two Non-Overlapping Subarrays
* 4 dp array tables, with length n + 1
* first dp table is the sum dp array, record sum to current index
* second dp table is the first length sum dp array, record max sum to current index
* third dp table is the second length sum dp array, record max sum to current index
* fourth dp table is the result max sum dp array, record max sum to current index
* base cases: 
  * array[0] = 0 for all arrays
  * firstLen dp array[i] = 0 for i less than first len
  * secondLen dp array[i] = 0 for i less than second len
  * result max dp array[i] = 0 for i less than first len + second len

* firstLen dp[i] = Math.max(dp[i - 1], sums[i] - sums[i - firstLen]) (continue first len sub array ending at i)
* secondLen dp[i] = Math.max(dp[i - 1], sums[i] - sums[i - secondLen]) (continue second len sub array ending at i)
* result max dp[i] is max of following:
  * dp[i-1] current num not a component of both firstLen and second Len array
  * (sums[i] - sums[i - firstLen]) + secondLen[i - firstLen]: current num is a component of first len array
  * (sums[i] - sums[i - secondLen]) + firstLen[i - secondLen]: current num is a component of second len array

* return last value of result max sum dp array

### LC 1186. Maximum Subarray Sum with One Deletion
* same as maximum subarray sum, with one extra variable to record the maximum sum with one deleted element(max1)
* on each loop the max1 equals to the max of (max1 + arr[i]) and max0;

### LC 1218. Longest Arithmetic Subsequence of Given Difference
* use a hash map to record the target(num - difference) subsequence length
* for every num, put num and value 1 to the map, then check if the target exists in map
* if target do exists, update the num value to the target value + 1 in map, and update the longest



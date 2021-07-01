### LC 1015. Smallest Integer Divisible by K
* first filter out impossible numbers: k % 2 or k % 5 == 0
* use a seen hash map to record remainders, if the remainder is seen, return -1
* init a remainder start with 0
* do a loop between [1, k], remainder = (remainder * 10 + 1) % K
* if remainder == 0, return i


### LC 1014. Best Sightseeing Pair
* use a left max pointer
* one pass, on each iteration, update the max score and check if the current value - distance is greater than max left value, if it is, update max left pointer
  
### LC 1131. Maximum of Absolute Value Expression
* transfer the original expression to four sub expressions
* return the result as max of the sub expressions

### LC 1262. Greatest Sum Divisible by Three
* use two sorted containers to sort the 2 smallest number that has modular 1 and 2 of mod 3
* calculate the sum and mod it by 3, and get answer by checking modular respectively

### LC 1558. Minimum Numbers of Function Calls to Make Target Array
* loop the array, if the current number is odd, decrement current number by 1, 奇数，add add operation count + 1
* if the number > 0 and is even, divide it by two, add multi operation count + 1
* each number will generate a multi operation, we maintain the max multi operation
* return max multi operation + add operation
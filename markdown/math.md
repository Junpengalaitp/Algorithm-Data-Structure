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
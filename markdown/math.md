### LC 1015. Smallest Integer Divisible by K
* first filter out impossible numbers: k % 2 or k % 5 == 0
* use a seen hash map to record remainders, if the remainder is seen, return -1
* init a remainder start with 0
* do a loop between [1, k], remainder = (remainder * 10 + 1) % K
* if remainder == 0, return i
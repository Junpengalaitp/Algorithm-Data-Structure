### LC 456. 132 Pattern
* use a variable to store left min value, init with nums[0]
* use a sorted map to store nums after nums[1].
* loop from nums[1], if ceiling left min + 1 key exists and is less than current num, return ture
* other wise update the map
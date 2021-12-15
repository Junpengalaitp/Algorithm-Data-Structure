### LC 456. 132 Pattern
* use a variable to store left min value, init with nums[0]
* use a sorted map to store nums after nums[1].
* loop from nums[1], if ceiling left min + 1 key exists and is less than current num, return ture
* other wise update the map

### LC 729. My Calendar I
* use a sorted set and sort by event start
* when booking, check floor and ceiling of new event and see there is any overlap
### LC 904. Fruit Into Baskets
* standard map counter approach, when map size > 2, shrink left

### LC 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
* two pointer approach, with a sorted map to record min and max values within the left and right interval

### LC 1574. Shortest Subarray to be Removed to Make Array Sorted
* two pointer start from left = 0 and right = 1
* move left forward until the arr[0:left] is not sorted
* if left == n - 1, return 0 (the arr is already sorted)
* move right backwards until arr[right:] is not sorted
* init res as min(right, n - left - 1) (min of removing whole left or right)
* do a while loop in the arr from the beginning to left index, and right < n
* if arr[i] <= arr[right], meaning arr[0:i] + arr[right:] is sorted, the answer is min (res, right - i - 1) (remove the middle part)
* else increment right by 1
### LC 81. Search in Rotated Sorted Array II
* check is binary search helpful
* find the sub arrays that pivot and target belong to

### LC 378. Kth Smallest Element in a Sorted Matrix
* binary search on mid value(not index), left start at top left, right start at bottom right
* for every mid value, count how many elements is smaller than the mid value
* if smaller elements count is greater than k, reduce right value by 1, else increment left value by 1 util left > right
* return left value

### LC 875. Koko Eating Bananas
* the max number of bananas per hour is the max of piles
* do a binary search from 1 to max number, find the minimum number of bananas that can finish piles
* the can finish function sum the hours, h += (piles[i] + mid - 1) / mid, return h is less or equal to t

### LC 1011. Capacity To Ship Packages Within D Days
* the max capacity to ship is the sum of packages
* do a binary search from 1 to max capacity, find the minimum capacity that can finish shipping
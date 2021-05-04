### LC 378. Kth Smallest Element in a Sorted Matrix
* binary search on mid value(not index), left start at top left, right start at bottom right
* for every mid value, count how many elements is smaller than the mid value
* if smaller elements count is greater than k, reduce right value by 1, else increment left value by 1 util left > right
* return left value
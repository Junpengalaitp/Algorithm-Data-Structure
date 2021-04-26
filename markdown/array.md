### LC 238. Product of Array Except Self
* use two arrays for storing left and right products
* multiply left and right products to get the result


## Two Pointers
### LC 15. 3Sum
* sort the num array, iterate every num, use the num as target and do a 2 sum on the remaining array
* if the target is larger than 0, break, and if the current num is the same with the previous one, skip it

### LC 80. remove duplicates from sorted array II
* init an index for write pointer, start with 0
* loop the array, if write pointer is less than 2 or  current num is not equal to write pointer - 2, set the current index element to be current num and increment write pointer

## 2D Array(Matrix)
### LC 48. Rotate image
* Transpose and Reverse: take the transpose of the matrix(pair change by diagonal), then reverse each row
* change layer by layer: in every layer, top left -> top right->bottom right->bottom left -> top left 


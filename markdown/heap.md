### LC 23. Merge k Sorted Lists
* put lists into the heap
* use next pointer to get next node

### LC 1046. Last Stone Weight
* add stones to a heap(reversed order)
* while heap size > 1, poll two stones out and calculate
* return heap top

### LC 295. Find Median from Data Stream
* use two heaps to store larger and smaller part of the data stream
* small heap, reversed order, large heap, natural order
* when total size is even, offer to larger heap and poll large heap top, offer it to small heap
* else offer to small heap and poll small heap top to large heap
* if total size is even, return avg of two heap tops, else return small heap top


### LC 857. Minimum Cost to Hire K Workers
* sort the workers by their wage / quality ratio
* use a max heap to select workers by their quality
* adding workers to the heap, if heap size == k, update the res to sum of quality  *  current worker ratio
* is heap size > k, poll the top and deduct the sumq accordingly

### LC 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows

### LC 719. Find K-th Smallest Pair Distance
* sort the nums, because the smallest distance must exist in the pairs of first kth nums
* loop the nums, offer the node to the heap, comparing the difference between current index and next index
* while k > 0, poll the heap, and if the node.next < nums.length - 1, offer new node(root, next + 1) to the heap
* return the node diff of heap top

### LC 632. Smallest Range Covering Elements from K Lists
* use heap to store the mins of each array, also record its index as pointers
* use a variable to store global max
* popping the heap, and update interval and variables

### LC 1675. Minimize Deviation in Array
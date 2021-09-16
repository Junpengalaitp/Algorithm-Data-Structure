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
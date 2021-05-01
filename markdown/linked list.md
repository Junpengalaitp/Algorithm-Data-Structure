### LC 147. Insertion Sort List
* base case: null or single node do nothing
* divide the list into two parts, sorted and unsorted, sorted pointer points to sorted tail, unsorted pointer points to unsorted head.
* use a sentinel to point head
* while unsorted head is not null, do the while loop, if unsorted head is larger than sorted tail, just move both pointers
* if unsorted head is smaller than sorted tail, start from the sentinel and to find a proper position to insert.

### LC 328. Odd Even Linked List
* use odd and even head, merge it in the end

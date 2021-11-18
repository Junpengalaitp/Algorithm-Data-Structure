### LC 146. LRU Cache
* A double linked list Node class that contains four fields
  * a key, used for removing node from the cache map when capacity reached
  * a value, to record value
  * prev pointer
  * next pointer

* LRU class contains four fields
  * capacity
  * a map for storing \<key, Node>
  * head node
  * tail node

* four methods for operating node 
  * addNode, add the node to the front of the linked list 
  * removeNode, remove a node from the linked list 
  * moveToFront, which is removeNode + addNode
  * popTail, remove and return the last node from the list

* put method
  * if key exists, update the node value and call moveToFront()
  * if map.size() reached capacity, call popTail(), and remove the node from the map using key field in node.
  * else create a new node and add the node to the cache and list

* get method
  * if key do not exist, return -1
  * return the node value and move the node to front

### LC 380. Insert Delete GetRandom O(1)
* back by a map and a list, map stores input as key, list index as value
* add: add input to list and store the value:index to map
* remove: 
  * get the list index of input value from map, set this index value to the the last element in the list
  * update map index of last value
  * remove the last element from list and map
* get random: get random element from list using random index


### LC 432. All O`one Data Structure
* two hash map and doubly linked list
* the linked list is an ascending sorted list, we always add count 1 node to the head
* when add key, if the key is not existing, simply add the the to the map with count 1 and add the node to the head
* when remove a key, if the key count is one, simply remove it from the maps and list
* if there key is existing before adding or after removing, we add a node with new count before/after current node, add remove the current node 


### LC 284. Peeking Iterator
* go one step forward, store the next in a variable
* hasNext(): return variable != null
* next(): store the variable in a tmp, update the variable to the next element, and return the variable
* peek(): return the variable

### LC 307. Range Sum Query - Mutable
* segment tree, O(logN)

### LC 352. Data Stream as Disjoint Intervals
* use a NavigableSet for storing the intervals in sorted order and get neighbors for merging, and a HashSet for filtering out the added numbers
* if the val is not in seen, add a new interval {val, val} to intervals, and call merge() on this new interval and try to merge with its neighbors
* recursively call this function to merge with neighbors, until there is no ligit neighbors to merge

### LC 355. Design Twitter
  
### Leetcode 146. LRU Cache
* A double linked list Node class that contains four fields
  * a key, used for removing node from cache map when reached capacity
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
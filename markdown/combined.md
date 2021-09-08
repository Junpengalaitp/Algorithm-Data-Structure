### LC 968. Binary Tree Cameras
* Tree Traversal(post order, the parent state is determined by its children) + DP(state machine)
* three states for a node
  * has camera: this node already placed a camera
  * covered: no camera here by covered by its parent of children
  * need cover: not covered by any camera

### LC 1372. Longest ZigZag Path in a Binary Tree
* dp + iterative tree traversal
* dp + recursive tree traversal

### LC 894. All Possible Full Binary Trees
* tree + backtracking, use a cache
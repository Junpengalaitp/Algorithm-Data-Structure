### LC 968. Binary Tree Cameras
* Tree Traversal + DP(state machine)
* three states for a node
  * has camera: this node already placed a camera
  * covered: no camera here by covered by its parent of children
  * need cover: not covered by any camera
## Binary Tree
### LC 94. Binary Tree Inorder Traversal
* Iterative
  * use a stack and while loop, the while loop condition is root != null or stack not empty.
  * in the while loop, use another while loop to add current root and it's left child to the stack.
  * when no left child(inside while ends), pop from the stack, add the value to result and sign current root = root.right

### LC 102. Binary Tree Level Order Traversal
* Iterative
  * use a queue and do a BFS, and each level only process current nodes in the queue
* Recursive
  * pass current level as a parameter in the recursive function.
  * if current level equals to result size, add a new list(level) to result;
  * add current root value to current level
  * recurse on left and right node

### LC 124. Binary Tree Maximum Path Sum
* the path can only choose one of the left and right subtree, so the helper returns root.val + max(left, right)
* in the helper, update the res to max(res, root.val + left + right)
* the left and right value are floored at 0, because a negative value would decrease the max value, so exclude it from the path

### LC 129. Sum Root to Leaf Numbers
* on recursive, update current num to current num * 10 + root.val
* if current node is a leaf node, add current num to result
* recurse on left and right child
### LC 131. Palindrome Partitioning
* backtracking approach
  * enumerate all possible substrings, and add the palindrome substrings subsets to result

* DP with backtracking approach
  * use a dp table, if the substring head equals to tail and the remaining string in the middle is also palindrome, current substring is a palindrome
### LC 110. Balanced Binary Tree
* approach 1(O(NlogN) time and space)
  * function 1: get height of every node
  * function 2:  use function 1check every node is balanced
  * main function: check root is balanced and call main function itself on left and right subtree
* approach 2: (logN time and space)
  * check balance at get height function, if it's not balanced, return an invalid value(exp:Integer.MIN_VALUE)
  * main function check is the root height equals invalid value

### LC 113. Path Sum II
* backtracking
  * base case 1: return on null node
  * add current node value to path
  * base case 2: if current node is a leaf node and its value equals to the remaining value, add new path to result and remove the last element in path
  * backtrack on left and right child with remaining value -= current node value
  * remove the last element in path

### LC 199. Binary Tree Right Side View
* level order traversal, use BFS and add each level's last value to result

### LC 236. Lowest Common Ancestor of a Binary Tree
* base case: if node is null or node is p or q, return node
* recursively call on left and right node
* return current node if left and right both not null
* if left is null, return right
* if right is null, return left

### LC 865,1123. Smallest Subtree with all the Deepest Nodes
* first find the deepest nodes use BFS, store them in a set
* find the lowest common ancestor of these nodes, same as LC 236. Lowest Common Ancestor of a Binary Tree

### LC 894. All Possible Full Binary Trees
* tree + backtracking, use a cache

### LC 513. Find Bottom Left Tree Value
* level level traversal
* can discard all upper levels to reduce memory usage

### LC 560, 783. Minimum Distance Between BST Nodes
* use inorder traversal
* when dealing with the root logic, if previous value is not null, update res, then replace previous value to current node value

### LC 563. Binary Tree Tilt
* use a global variable to store the tilt
* base case: null node returns 0
* on traversal, increment the tilt value by abs(left + right)
* return the sum of (left + right + node.val) as the traversal function return value

### LC 654. Maximum Binary Tree
* find the max index in the nums array between left and right index
* base case: left >= right, return null, because max right = nums.length, so if left == right, has to stop
* recurse on left index to max index and max index + 1 to right index

### LC 987. Vertical Order Traversal of a Binary Tree
* do a traversal and mark each node's coordinates
* build answer by the coordinates, col are levels, and in each level order nodes val by comparing order row -> val

### LC 1104. Path In Zigzag Labelled Binary Tree
* a full binary tree characteristics problem

### LC 1261. Find Elements in a Contaminated Binary Tree
* tree traversal and recover the binary tree
* in traversal, add value to a set

### LC 1302. Deepest Leaves Sum
* BFS get the last level
* return last level sum

### LC 1372. Longest ZigZag Path in a Binary Tree
* dp + iterative tree traversal
  * two dp maps for recording current path length of left and right children
  * because of ZigZag, the left node path length is its parent length in right map + 1, and vice versa for right node;
  * in the traversal, update the res to max(res, left len, right len)
* dp + recursive tree traversal
  * pre order, update the max length, then traversal the left and right children
  * left: length + 1 if the direction is right, else length = 1
  * right: length + 1 if the direction is left, else length = 1 

## Binary Search Tree
### LC 95. Unique Binary Search Trees II
* recursion approach, recursive call on (start, i - 1) and (i + 1, end), the i is the current BST root

### LC 99. Recover Binary Search Tree
* do a inorder traversal, add nodes to a list
* find two nodes in the list
* swap their values

### LC 98. Validate Binary Search Tree
* recursive approach, init with lower bound of MIN_VALUE and upper bound of MAX_VALUE
* base case: null root is valid
* false case: current root value in not in the bound
* recurse on left child with upper bound of current root value, and recurse on right child with lower bound of current root value

### LC 230. Kth Smallest Element in a BST
* use iterative inorder traversal, when popping front the stack, if k == 1, return the root value, if not, 
  decrement k by 1 and continue the inorder traversal

### LC 450. Delete Node in a BST
* if current root value != key, recurse on left or right child(root.left = (recurse on left), root.right = (recurse on right)), depending on the root value less or greater than root value.
* if current root value == key, if current root is a leaf node, remove it.
* if the current root has no left child, return right child
* if the current root has no right child, return left child
* if the current root has both children, find the smallest node that is greater than current root
* replace current root value with the smallest node value, and delete the smallest node by point its parent's left child to grand right child
* if parent == root, meaning that it has no grand left child, replace the right to grand right child

### LC 669. Trim a Binary Search Tree
* preorder traversal
* if root.val < low, return result of it's right
* if root.val > high, return result of it's left
* recurse on left and right child
* can also be done with postorder traversal

### LC 1022. Sum of Root To Leaf Binary Numbers
* on recursion, add current value to binary string
* convert binary string to int and add it to result if it's a leaf node
* recursion on left and right pass the binary string as a variable
### LC 1008. Construct Binary Search Tree from Preorder Traversal
* add values to a deque, or just use input array with index to save space
* use preorder traversal, pass min and max value in helper as params
* if the deque is empty or deque first is out of min,max bound, return null
* remove the top value from deque as the TreeNode
* recurse on left and right and update params use current value

### LC 1373. Maximum Sum BST in Binary Tree
* traversal from the root, if the current root is BST, sum the nodes value and update max
* isBST(): check node value is strictly between min and max, and left and right children are also BSTs
* treeSum(): return the sum value of the node value and treeSum(left) and treeSum(right), and update the maxSum

### LC 1448. Count Good Nodes in Binary Tree
* global res
* if the node value is equal or greater than path max value, res++
* recursion on left and right node with max of (max, node value)
## Morris Traversal
* LC 99. Recover Binary Search Tree




## Inorder Traversal
* LC 560, 783. Minimum Distance Between BST Nodes



### LC 314. Binary Tree Vertical Order Traversal
* normal tree traversal with a coordinate to mark row and col
* use a SortedMap to get output in order, O(nlogn) time
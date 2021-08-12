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
* if the left or right is less than 0, use 0 as value

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

### LC 513. Find Bottom Left Tree Value
* level level traversal
* can discard all upper levels to reduce memory usage

### LC 987. Vertical Order Traversal of a Binary Tree
* do a traversal and mark each node's coordinates
* build answer by the coordinates, col are levels, and in each level order nodes val by comparing order row -> val

### LC 1104. Path In Zigzag Labelled Binary Tree
* a full binary tree characteristics problem

### LC 1261. Find Elements in a Contaminated Binary Tree
* tree traversal and recover the binary tree
* in traversal, add value to a set

## Binary Search Tree
### LC 95. Unique Binary Search Trees II
* recursion approach, recursive call on (start, i - 1) and (i + 1, end), the i is the current BST root

### LC 98. Validate Binary Search Tree
* recursive approach, init with lower bound of MIN_VALUE and upper bound of MAX_VALUE
* base case: null root is valid
* false case: current root value in not in the bound
* recurse on left child with upper bound of current root value, and recurse on right child with lower bound of current root value

### LC 230. Kth Smallest Element in a BST
* use iterative inorder traversal, when popping front the stack, if k == 1, return the root value, if not, 
  decrement k by 1 and continue the inorder traversal

### LC 1302. Deepest Leaves Sum
* BFS get the last level
* return last level sum

### LC 1372. Longest ZigZag Path in a Binary Tree
* 

### LC 1373. Maximum Sum BST in Binary Tree
* traversal from the root, if the current root is BST, sum the nodes value and update max
* isBST(): check node value is strictly between min and max, and left and right children are also BSTs
* treeSum(): return the sum value of the node value and treeSum(left) and treeSum(right), and update the maxSum



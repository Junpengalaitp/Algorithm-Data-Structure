## Binary Tree
### LC 94. Binary Tree Inorder Traversal
* Iterative
  * use a stack and while loop, the while loop condition is root != null or stack not empty.
  * in the while loop, use another while loop to add current root and it's left child to the stack.
  * when no left child(inside while ends), pop from the stack, add the value to result and sign current root = root.right

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

## Binary Search Tree
### 95. Unique Binary Search Trees II
* recursion approach, recursive call on (start, i - 1) and (i + 1, end), the i is the current BST root

### 98. Validate Binary Search Tree
* recursive approach, init with lower bound of MIN_VALUE and upper bound of MAX_VALUE
* base case: null root is valid
* false case: current root value in not in the bound
* recurse on left child with upper bound of current root value, and recurse on right child with lower bound of current root value
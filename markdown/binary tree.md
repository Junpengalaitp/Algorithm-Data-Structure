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
  * main function: check root is balaced and call main function itself on left and right subtree
* approach 2: (logN time and space)
  * check balance at get height function, if it's not balanced, return an invalid value(exp:Integer.MIN_VALUE)
  * main function check is the root height equals invalid value
# Trie
### LC 208. Implement Trie (Prefix Tree)
* Define a trie node class, which is a tree node that has multiple children(recorded using a map),
  and a boolean value for marking whether the current trie node is an end of a word
* all operations breaks input word into chars, and start from the root node.
* if current node is not matching current char, the operations return false, else continue on its children

### LC 211. Design Add and Search Words Data Structure
* use a trie
* search operation use dfs for handling '.' wild card
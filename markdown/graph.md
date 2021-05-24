# DFS & BFS
### LC 200. Number of Islands
* loop the grid, start search when encountering island, and increment the number of islands by 1
* can change the visited island to '2' instead of visited hash table.


### LC 886. Possible Bipartition
* mark adjacent nodes to two opposite color
* do a graph traversal, if encounter adjacent nodes with same color, return false
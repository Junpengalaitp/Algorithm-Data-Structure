# DFS & BFS
### LC 200. Number of Islands
* loop the grid, start search when encountering island, and increment the number of islands by 1
* can change the visited island to '2' instead of visited hash table.

### LC 785. Is Graph Bipartite?
* use a color map to record node and its color, and this map also work as a visited map
* for every node in the graph, do a dfs starting at the node, each time in dfs, flip the color (represented by -1 and 1)
* dfs base case: node already in the map, return the current color equals to color in the map
### LC 886. Possible Bipartition
* mark adjacent nodes to two opposite color
* do a graph traversal, if encounter adjacent nodes with same color, return false


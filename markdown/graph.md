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

### LC 947. Most Stones Removed with Same Row or Column
* build a doubly linked graph from stones if stones row or col are the same
* do a dfs/bfs for every stone, increment one for every connected stone in graph
* at the end of dfs/bfs, decrement res by one, because it cannot remove itself

### LC 1020. Number of Enclaves
* do a dfs/bfs the 1s on edges, mark connected 1s to -1
* count how many 1s left in the gird as answer


### LC 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
* Floyd-Warshall algorithm


### LC 834. Sum of Distances in Tree
* treat the tree as a graph
* do two different df on the graph and get ans

### LC 743. Network Delay Time

### LC 815. Bus Routes
* each route is a node, build a undirected graph on routes if two routes has intersections
* use a bfs to get the shortest route
* add depth and route as node to the queue
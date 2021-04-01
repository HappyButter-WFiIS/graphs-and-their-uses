from array import *
 
graph1 = [[1,3,4],[7,2,0],[3,6,1],[0,5,2],[0,7,5],[4,6,3],[7,5,2],[1,4,6]]  # adjacency list
graph2 = [[1,2,3,4,5], [0], [0], [0,4,5], [0,3,5], [0,3,4]]                 # adjacency list
 
def isHamiltonianPathFromVertex(G, visited, curr_vertex) -> int:
    visited[curr_vertex] = 1
    if not 0 in visited:
        return 1
    for v in G[curr_vertex]:
        if not visited[v]:
            if isHamiltonianPathFromVertex(G,visited,v): return 1
    visited[curr_vertex] = 0
    return 0
 
def isHamiltonian(G) -> int:
    visited = [0] * len(G)
    for v in range(len(G)):
        if(isHamiltonianPathFromVertex(G, visited, v) ):
            return 1
        visited = [0] * len(G)
    return 0
 
print(isHamiltonian(graph1))  # output 1 means graph is hamiltonian
print(isHamiltonian(graph2))  # output 0 means graph is not hamiltonian
from array import *

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
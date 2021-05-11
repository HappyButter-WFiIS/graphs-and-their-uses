from array import *

def isHamiltonianPathFromVertex(G: list, visited: list, curr_vertex: int) -> int:
	"""
    Check if exists hamiltonian path starting from curr_vertex
	Returns 1 if hamiltonian path from curr_vertex exists, otherwise 0 
    Parameters: 
        G - representation of graph as adjecency list
        visited - list that keeps info about already visited nodes
        curr_vertex - starting vertex
	"""
    visited[curr_vertex] = 1
    if not 0 in visited:
        return 1
    for v in G[curr_vertex]:
        if not visited[v]:
            if isHamiltonianPathFromVertex(G,visited,v): return 1
    visited[curr_vertex] = 0
    return 0

def isHamiltonian(G: list) -> int:
	"""
    Check if exists hamiltonian path in graph G
	Returns 1 if hamiltonian path exists, otherwise 0 
    Parameters: 
        G - representation of graph as adjecency list
	"""
    visited = [0] * len(G)
    for v in range(len(G)):
        if(isHamiltonianPathFromVertex(G, visited, v) ):
            return 1
        visited = [0] * len(G)
    return 0

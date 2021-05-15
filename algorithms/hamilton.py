"""
    algorithm to find hamiltonian cycle
    input is adjacency matrix
"""
 
from typing import List
 
 
# Checks whether it is possible to add next vertex
def valid_connection(
    graph: List[List[int]], next_ver: int, curr_ind: int, path: List[int]) -> bool:
    if graph[path[curr_ind - 1]][next_ver] == 0:
        return False
    return not any(vertex == next_ver for vertex in path)
 
 
# Chceck if we visited all of vertices
# If last visited vertex has path to starting vertex return True
# either return False
 
def hamilton_inner(graph: List[List[int]], path: List[int], curr_ind: int) -> bool:
    if curr_ind == len(graph):
        return graph[path[curr_ind - 1]][path[0]] == 1
    for next in range(0, len(graph)):
        if valid_connection(graph, next, curr_ind, path):
            path[curr_ind] = next
            if hamilton_inner(graph, path, curr_ind + 1):
                return True
            path[curr_ind] = -1
    return False
 
 
def hamilton(graph: List[List[int]], initial_vertex: int = 0) -> List[int]:
    path = [-1] * (len(graph) + 1)
    path[0] = path[-1] = initial_vertex
    return path if hamilton_inner(graph, path, 1) else []

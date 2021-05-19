from copy import deepcopy
from utils.Graph import Graph, RepresentationType

def dfs(adjlist: list, vertex: int, visited: list, stack: list) -> list:
    """
    Visits vertices using recursive DFS algorithm 
    and appends visited nodes to stack.
    Parameters:
        adjlist - representation of graph as adjecency list (for finding neighbours)
        vertex - node which is visited in certain DFS invocation
        visited - list of visited vetrices
        stack - stack containing visited and processed nodes
    """
    visited[vertex] = True
    for x in adjlist[vertex]:
        if visited[x - 1] == False:
            dfs(adjlist, x - 1, visited, stack)
    
    stack.append(vertex)            


def transpose(G: Graph) -> Graph:
    """
    Creates transpose graph of given directed graph.
    """
    T = Graph()
    adjlist = [[] for _ in range(len(G.repr))]
    
    for i in range(len(G.repr)):
        for x in G.repr[i]:
            adjlist[x - 1].append(i + 1)
            
    T.load_data(adjlist, RepresentationType.ADJACENCY_LIST)
    return T


def print_group(group: list, index: int) -> None:
    """
    Prints strongly connected component.
    """
    print(str(index + 1) + ') ' + ' '.join([str(x + 1) for x in group]))
    
    
def kosaraju(G: Graph) -> list:
    """
    Finds strongly connected components in directed graphs
    using Kosaraju algorithm.
    """
    G.to_adjacency_list()
    visited = [False for _ in range(len(G.repr))]
    stack = []
    
    for i in range(len(G.repr)):
        if visited[i] == False:
            dfs(G.repr, i, visited, stack)
    
    T = transpose(G)
    stack.reverse()
    visited = [False for _ in range(len(G.repr))]
    groups = [0 for _ in range(len(G.repr))]
    group = []
    index = 0
    
    for i in stack:
        if visited[i] == False:
            dfs(T.repr, i, visited, group)
            for x in group:
                groups[x] = index
                
            print_group(group, index)
            group = []    
            index += 1

    return groups
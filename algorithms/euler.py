from random import randint
from copy import deepcopy
from utils.graph_generators import get_graph_with_probability
from utils.Graph import Graph, RepresentationType


def dfs(adj_mat: list, adj_list: int, vertex: int) -> list:
    """
    Finds Euler cycle using DFS algorithm without recursion (thus using stack).
    Returns sequence of vertices in Euler Cycle.
    Parameters: 
        adj_mat - representation of graph as adjecency matrix (for deleting edges)
        adj_list - representation of graph as adjecency list (for finding neighbours)
        vertex - initial node, beginning of the cycle
    """
    stack = [vertex]
    cycle = []
    position = [0 for _ in range(len(adj_list))]

    while stack != []:
        vertex = stack.pop()
        
        while position[vertex] < len(adj_list[vertex]):
            v = adj_list[vertex][position[vertex]] - 1
            position[vertex] += 1

            if adj_mat[vertex][v] == 0:
                continue
            else:
                stack.append(vertex)
                adj_mat[vertex][v] = 0
                adj_mat[v][vertex] = 0
                vertex = v
        
        cycle.append(str(vertex + 1))
    
    return cycle
    

def euler_cycle(G: Graph) -> str:
    """
    Returns string representing Euler Cycle 
    in Euler Graph given as a parameter.
    """
    copyG = deepcopy(G)

    copyG.to_adjacency_matrix()
    adj_mat = copyG.repr
    copyG.to_adjacency_list()
    adj_list = copyG.repr

    cycle = dfs(adj_mat, adj_list, 0)
    return '[' + ' - '.join(cycle) + ']'


def generate_euler_graph_sequence(G: Graph, vertices: int) -> bool:
    """
    Generates graphical sequence of Euler Graph for given number of vertices 
    and loads it to graph given as a parameter.
    Returns True if generating was successful in one of num_samples iterations.
    """
    num_samples = 100
    iteration = 0

    while iteration < num_samples:
        graphical_sequence = [(randint(2, vertices-1) // 2) * 2 for _ in range(vertices)]

        if G.load_data(graphical_sequence, RepresentationType.GRAPH_SEQUENCE):
            return True

        iteration += 1              

    return False
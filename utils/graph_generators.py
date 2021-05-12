import numpy as np
import random
from utils.Graph import RepresentationType, Graph
from array import *


def get_graph_by_vertices_and_edges(num_of_vertices: int, num_of_edges: int) -> list:
    """
    Return graph, represented by an incidence matrix, with nodes,
    which amount is passed by 'num_of_nodes' parameter. These nodes,
    are linked with randomly chosen edges in a number of 'num_of_edges'.
    """
    # handling incorrect number of vertices
    if num_of_vertices < 1:
        print("Number of vertices must be positive.")
        num_of_vertices = 1
    
    # handling incorrect number of edges
    max_edges_number = num_of_vertices * (num_of_vertices-1) // 2
    if num_of_edges > max_edges_number:
        print("\nMax number of edges for graph with {0} vertices is {1}".format(num_of_vertices, max_edges_number))
        print("-> Generating graph with {0} edges.".format(max_edges_number))
        num_of_edges = max_edges_number
    elif num_of_edges < 0:
        print("\nMin number of edges is 0".format(num_of_vertices, max_edges_number))
        print("-> Generating graph with 0 edges.")
        num_of_edges = 0
        
    
    vertices_list = list(range(0, num_of_vertices))
    edges_list = [(a, b) for idx, a in enumerate(vertices_list) for b in
                  vertices_list[idx + 1:]]  # at the beginning all possible edges

    while len(edges_list) > num_of_edges:
        # randomly remove edges to match required number
        random_item_from_edges_list = random.choice(edges_list)
        edges_list.remove(random_item_from_edges_list)

    graph = [[0] * num_of_edges for i in range(num_of_vertices)]
    for i in range(num_of_edges):
        graph[edges_list[i][0]][i] = 1  # create graph as incidence matrix
        graph[edges_list[i][1]][i] = 1
    return graph


def get_graph_with_probability(num_of_nodes: int, probability: float) -> list:
    """
    Return graph, represented by 'num_of_nodes' x 'num_of_nodes'
    adjacency matrix, with connections between nodes, that
    depend on the 'probability' parameter.
    """
    # handle if number of nodes is not in range (1;1000) 
    if num_of_nodes > 1000:
        print("\nIt may take a few seconds... Relax...")  
    elif num_of_nodes < 1:
        print("\nMin number of nodes is 1")
        print("-> Generating graph with 1 node.")
        num_of_nodes = 1 
    
    graph = np.random.random((num_of_nodes, num_of_nodes))
    graph = graph >= 1 - probability

    for i in range(num_of_nodes):
        graph[i][i] = False

    for i in range(num_of_nodes):
        for j in range(i+1):
            graph[i][j] = graph[j][i]

    return np.asarray(graph, dtype=int).tolist()


def traverse(u: int, visited: list, G: list):
    visited[u] = 1
    for v in range(len(G)):
        if (G[u][v]):
            if not (visited[v]):
                traverse(v, visited, G)


def isConnected(G: list) -> bool:
    visited = [0]*len(G)
    for u in range(len(G)):
        for i in range(len(G)):
            visited[i] = 0
        traverse(u, visited, G)
        for i in range(len(G)):
            if not (visited[i]):
                return 0
    return 1


# size is num of vertices
def gen_random_conn_graph_weighted(size: int) -> list:
    flag = 1
    while flag == 1:
        G = [[0] * size for i in range(size)]
        p = random.randint(1, 10)  # more or less roll graph density here

        for i in range(size):
            for j in range(size):
                if random.randint(1, 10) <= p:
                    G[i][j] = random.randint(1, 10)

        for i in range(size):               #
            for j in range(size):           # making matrix
                if (j == i):
                    G[i][j] = 0    # symetric
                if (j < i):
                    G[i][j] = G[j][i]
        if isConnected(G):
            return G


def randomize(G: Graph, randomizations: int):
    """
    Swap connections between randomly chosen nodes.
    The amount of replacements made is determined by the 'randomizations' argument.
    """

    completed_randomizations = 0
    iterations = 0

    while completed_randomizations < randomizations:
        edges = []
        iterations += 1
        if iterations > 10*randomizations:
            return

        for i in range(len(G.repr)):
            for j in range(i):
                if G.repr[i][j]:
                    edges.append((i, j))

        if edges:
            first_edge = edges[np.random.randint(len(edges))]
            second_edge = edges[np.random.randint(len(edges))]

            a, b = first_edge
            c, d = second_edge

            if G.repr[a][d] or G.repr[c][b] or a == d or b == c:
                continue
            else:
                G.repr[a][b] = G.repr[b][a] = 0
                G.repr[c][d] = G.repr[d][c] = 0
                G.repr[a][d] = G.repr[d][a] = 1
                G.repr[c][b] = G.repr[b][c] = 1
                completed_randomizations += 1

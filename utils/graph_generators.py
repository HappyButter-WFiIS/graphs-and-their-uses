import numpy as np
import random
from array import *


def get_graph_by_vertices_and_edges(num_of_vertices: int, num_of_edges: int):
    vertices_list = list(range(0, num_of_vertices))
    edges_list = [(a, b) for idx, a in enumerate(vertices_list) for b in
                  vertices_list[idx + 1:]]  # at the beginning all possible edges

    while len(edges_list) > num_of_edges:
        random_item_from_edges_list = random.choice(edges_list)  # randomly remove edges to match required number
        edges_list.remove(random_item_from_edges_list)

    graph = [[0] * num_of_edges for i in range(num_of_vertices)]
    for i in range(num_of_edges):
        graph[edges_list[i][0]][i] = 1  # create graph as incidence matrix
        graph[edges_list[i][1]][i] = 1
    return graph


def get_graph_with_probability(num_of_nodes: int, probability: float) -> np.ndarray:
    graph = np.random.random((num_of_nodes, num_of_nodes))
    graph = graph >= 1 - probability

    for i in range(num_of_nodes):
        graph[i][i] = False

    for i in range(num_of_nodes):
        for j in range(i+1):
            graph[i][j] = graph[j][i]

    return np.asarray(graph, dtype=int)



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


def gen_random_conn_graph_weighted(size: int) -> list:  # size is num of vertices
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


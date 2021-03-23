import numpy as np
import random


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
    return np.asarray(graph, dtype=int)

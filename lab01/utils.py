import numpy as np


def get_graph_with_probability(n, probability):
    graph = np.random.random((n, n))
    graph = graph >= probability
    for i in range(n):
        graph[i][i] = False
    return graph

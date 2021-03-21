import numpy as np


def get_graph_with_probability(num_of_nodes: int, probability: float) -> np.ndarray:
    graph = np.random.random((num_of_nodes, num_of_nodes))
    graph = graph >= 1 - probability

    for i in range(num_of_nodes):
        graph[i][i] = False
    return graph


if __name__ == '__main__':
    print(get_graph_with_probability(10, 1))

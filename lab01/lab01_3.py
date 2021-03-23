import os
import numpy as np

from utils.GraphRepresentation import GraphRepresentation, RepresentationType
from utils.GraphPlotter import plot_graph
from utils.graph_generators import get_graph_with_probability


if __name__ == "__main__":
    G = GraphRepresentation()
    data = get_graph_with_probability(7, 0.5)
    np.savetxt('temp.txt', data, fmt='%.0f')

    G.create_representation('temp.txt', representation_type=RepresentationType.ADJACENCY_MATRIX)
    plot_graph(G.repr)
    os.remove('temp.txt')
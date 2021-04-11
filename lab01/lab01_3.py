import os, sys
import numpy as np

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.GraphRepresentation import GraphRepresentation, RepresentationType
from utils.GraphPlotter import plot_graph
from utils.graph_generators import get_graph_with_probability, get_graph_by_vertices_and_edges


if __name__ == "__main__":
    G = GraphRepresentation()
    data = get_graph_with_probability(7, 0.5)

    # overkill -> GraphRepresentation is ready to create from get_graph_with_probability method result which is np.ndarray

    # np.savetxt('temp.txt', data, fmt='%.0f')
    # G.create_representation('temp.txt', representation_type=RepresentationType.ADJACENCY_MATRIX)

    G.load_data(data=data.tolist(), representation_type=RepresentationType.ADJACENCY_MATRIX)
    print(G)
    plot_graph(G.repr)

    G = GraphRepresentation()
    data = np.matrix(get_graph_by_vertices_and_edges(5, 8))

    # np.savetxt('temp.txt', data, fmt='%.0f')
    # G.create_representation('temp.txt', representation_type=RepresentationType.INCIDENCE_MATRIX)
    
    G.load_data(data=data.tolist(), representation_type=RepresentationType.INCIDENCE_MATRIX)
    G.to_adjacency_matrix()
    print(G)
    plot_graph(G.repr)

    # os.remove('temp.txt')

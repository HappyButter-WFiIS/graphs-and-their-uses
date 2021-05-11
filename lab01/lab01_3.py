import os, sys
import numpy as np

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import plot_graph
from utils.graph_generators import get_graph_with_probability, get_graph_by_vertices_and_edges


if __name__ == "__main__":
    G = Graph()
    data = get_graph_with_probability(7, 0.5)

    G.load_data(data=data, representation_type=RepresentationType.ADJACENCY_MATRIX)
    print(G)
    plot_graph(G)

    G = Graph()
    data = get_graph_by_vertices_and_edges(5, 8)

    G.load_data(data=data, representation_type=RepresentationType.INCIDENCE_MATRIX)
    G.to_adjacency_matrix()
    print(G)
    plot_graph(G)

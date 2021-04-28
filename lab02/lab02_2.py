import os, sys
import numpy as np

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.GraphRepresentation import GraphRepresentation, RepresentationType
from utils.graph_plotter import plot_graph
from utils.graph_generators import randomize


if __name__ == "__main__":
    G = GraphRepresentation()
    G.load_data([4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2], RepresentationType.GRAPH_SEQUENCE)
    G.to_adjacency_matrix()

    # plot_graph(G.repr)
    for _ in range(1000):
        randomize(G)
    plot_graph(G.repr)

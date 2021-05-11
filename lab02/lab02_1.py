import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.graph_plotter import plot_graph
from utils.Graph import Graph, RepresentationType


if __name__ == '__main__':
    G = Graph()
    G.load_data([4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2], RepresentationType.GRAPH_SEQUENCE)

    G.to_adjacency_matrix()

    plot_graph(G)
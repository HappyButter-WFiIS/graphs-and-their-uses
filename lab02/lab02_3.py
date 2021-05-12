import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import GraphPlotter
from algorithms.components import get_components, print_sorted_components


if __name__ == '__main__':
    G = Graph()
    G.load_data([2, 2, 2, 1, 3, 1, 2, 1, 4, 2, 2, 1, 3, 1, 1],
                RepresentationType.GRAPH_SEQUENCE)
    G.to_adjacency_list()
    groups = get_components(G)

    print_sorted_components(G, groups)
    G.to_adjacency_matrix()
    GraphPlotter.plot_graph(G, groups)

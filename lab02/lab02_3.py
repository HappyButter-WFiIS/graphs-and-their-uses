import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import plot_graph
from algorithms.components import search, sort_groups


if __name__ == '__main__':
    G = Graph()
    G.load_data([4, 2, 2, 3, 1, 3, 4, 1, 2, 2, 2],
                RepresentationType.GRAPH_SEQUENCE)
    G.to_adjacency_list()
    groups = search(G)

    sort_groups(G, groups)
    G.to_adjacency_matrix()
    plot_graph(G, groups)

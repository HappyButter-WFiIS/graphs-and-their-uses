import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.DirectedGraph import DirectedGraph, RepresentationType
from utils.graph_plotter import GraphPlotter
from utils.graph_generators import get_directed_graph_with_probability
from algorithms.kosaraju import kosaraju

if __name__ == '__main__':
    G = DirectedGraph()

    G.load_data(get_directed_graph_with_probability(10, 0.2, 1, 1), RepresentationType.ADJACENCY_MATRIX)
    groups = kosaraju(G)
    GraphPlotter.plot_graph(G, draw_wages = False, draw_arrows = True, nodes_color_modes = groups)
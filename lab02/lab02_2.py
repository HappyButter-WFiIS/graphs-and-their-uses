import os, sys
import numpy as np

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import GraphPlotter
from utils.graph_generators import randomize


if __name__ == "__main__":
    randomizations = 1000
    G = Graph()
    G.load_data([4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2], RepresentationType.GRAPH_SEQUENCE)
    G.to_adjacency_matrix()

    randomize(G, randomizations)
    GraphPlotter.plot_graph(G)

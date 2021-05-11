import os, sys
import numpy as np

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import GraphPlotter
from utils.graph_generators import randomize

if __name__ == "__main__":
    G = Graph()

    G.create_k_regular_with_n_vertices(k=2, vertices=7)
    randomize(G, 100)

    GraphPlotter.plot_graph(G)


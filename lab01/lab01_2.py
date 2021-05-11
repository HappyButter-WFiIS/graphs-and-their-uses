import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import GraphPlotter

if __name__ == "__main__":
    G = Graph()
    G.create_representation(os.path.dirname(__file__) + '/inputs/adjmat.txt', RepresentationType.ADJACENCY_MATRIX)
    GraphPlotter.plot_graph(G)

    G.create_representation(os.path.dirname(__file__) + '/inputs/incmat.txt', RepresentationType.INCIDENCE_MATRIX)
    GraphPlotter.plot_graph(G)

    G.create_representation(os.path.dirname(__file__) + '/inputs/adjlist.txt', RepresentationType.ADJACENCY_LIST)
    GraphPlotter.plot_graph(G)

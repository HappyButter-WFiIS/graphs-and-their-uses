import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.GraphRepresentation import GraphRepresentation, RepresentationType
from utils.graph_plotter import plot_graph

if __name__ == "__main__":
    G = GraphRepresentation()
    G.create_representation(os.path.dirname(__file__) + '/inputs/adjmat.txt', RepresentationType.ADJACENCY_MATRIX)
    plot_graph(G.repr)

    G.create_representation(os.path.dirname(__file__) + '/inputs/incmat.txt', RepresentationType.INCIDENCE_MATRIX)
    G.to_incidence_matrix()
    plot_graph(G.repr)
    
    G.create_representation(os.path.dirname(__file__) + '/inputs/adjlist.txt', RepresentationType.ADJACENCY_LIST)
    G.to_incidence_matrix()
    plot_graph(G.repr)

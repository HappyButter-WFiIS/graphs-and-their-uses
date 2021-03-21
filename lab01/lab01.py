import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from graph.representations.GraphRepresentation import GraphRepresentation, RepresentationType
from graph.representations.GraphPlotter import plot_graph

if __name__ == "__main__":
    G = GraphRepresentation()
    G.create_representation(os.path.dirname(__file__) + '/files/adjmat.txt', RepresentationType.ADJACENCY_MATRIX)
    
    # plotter usage
    plot_graph(G.repr)

    G.to_adjacency_list()
    G.to_incidence_matrix()
    G.create_representation(os.path.dirname(__file__) + '/files/incmat.txt', RepresentationType.INCIDENCE_MATRIX)
    G.to_adjacency_list()
    G.to_adjacency_matrix()
    G.create_representation(os.path.dirname(__file__) + '/files/adjlist.txt', RepresentationType.ADJACENCY_LIST)
    G.to_adjacency_matrix()
    G.to_incidence_matrix()
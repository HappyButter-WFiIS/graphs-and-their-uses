import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.GraphRepresentation import GraphRepresentation, RepresentationType

if __name__ == "__main__":
    G = GraphRepresentation()
    G.create_representation(os.path.dirname(__file__) + '/inputs/adjmat.txt', RepresentationType.ADJACENCY_MATRIX)
    print(G)
    G.to_adjacency_list()
    print(G)
    G.to_incidence_matrix()
    print(G)

    G.create_representation(os.path.dirname(__file__) + '/inputs/incmat.txt', RepresentationType.INCIDENCE_MATRIX)
    print(G)
    G.to_adjacency_list()
    print(G)
    G.to_adjacency_matrix()
    print(G)
    
    G.create_representation(os.path.dirname(__file__) + '/inputs/adjlist.txt', RepresentationType.ADJACENCY_LIST)
    print(G)
    G.to_adjacency_matrix()
    print(G)
    G.to_incidence_matrix()
    print(G)

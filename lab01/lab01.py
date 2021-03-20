import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from graph.representations.GraphRepresentation import GraphRepresentation, RepresentationType

if __name__ == "__main__":
    G = GraphRepresentation()
    G.create_representation(os.path.dirname(__file__) + '/files/adjmat.txt', RepresentationType.ADJACENCY_MATRIX)
    G.create_representation(os.path.dirname(__file__) + '/files/incmat.txt', RepresentationType.INCIDENCE_MATRIX)
    G.create_representation(os.path.dirname(__file__) + '/files/adjlist.txt', RepresentationType.ADJACENCY_LIST)
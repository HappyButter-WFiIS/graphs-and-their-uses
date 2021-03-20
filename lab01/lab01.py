import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from graph.representations.GraphRepresentation import GraphRepresentation

if __name__ == "__main__":
    G = GraphRepresentation()
    G.create_adjacency_matrix(os.path.dirname(__file__) + '/files/adjmat.txt')
    G.create_incidence_matrix(os.path.dirname(__file__) + '/files/incmat.txt')
    G.create_adjacency_list(os.path.dirname(__file__) + '/files/adjlist.txt')

    
    
    


        
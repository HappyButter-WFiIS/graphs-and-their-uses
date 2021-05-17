import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from algorithms.hamilton import hamilton

if __name__ == '__main__':
    G = Graph()
    
    G.load_data([[0, 1, 0, 1, 0],[1, 0, 1, 1, 1],[0, 1, 0, 0, 1],[1, 1, 0, 0, 1],[0, 1, 1, 1, 0]], \
    			RepresentationType.ADJACENCY_MATRIX)  #adjacency matrix
    print(hamilton(G))
 
    G.load_data([[0, 1, 0, 1, 0], [1, 0, 1, 1, 1],[0, 1, 0, 0, 1],[1, 1, 0, 0, 0], [0, 1, 1, 0, 0]], \
     			RepresentationType.ADJACENCY_MATRIX)  #adjacency matrix
    print(hamilton(G))

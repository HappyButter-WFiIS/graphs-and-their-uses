import os, sys, copy

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.GraphRepresentation import GraphRepresentation, RepresentationType
from utils.GraphPlotter import plot_graph
from algorithms.euler import euler_cycle

if __name__ == "__main__":
    #v = input('Number of vertices: ')

    #----->test
    G = GraphRepresentation()
    G.create_representation(os.path.dirname(__file__) + '/inputs/test4.txt', RepresentationType.ADJACENCY_LIST)
    print(euler_cycle(copy.deepcopy(G.repr)))
    G.to_adjacency_matrix()
    plot_graph(G.repr)
    #----------




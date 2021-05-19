import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import GraphPlotter
from algorithms.kosaraju import kosaraju

if __name__ == '__main__':
    G = Graph()
    G.load_data([[0,1,0,0,1,0,0,0,0],
                 [0,0,1,0,0,0,0,0,0],
                 [0,0,0,0,0,1,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,1,0,1,0,1,1,1,0],
                 [0,0,0,0,0,0,0,0,1],
                 [0,0,0,0,1,0,0,0,0],
                 [0,0,0,0,0,0,1,0,0],
                 [0,0,0,0,1,0,0,1,0]], RepresentationType.ADJACENCY_MATRIX) #example
    
    groups = kosaraju(G)
    GraphPlotter.plot_graph(G, groups)
    print('')
    
    G.load_data([[0, 1, 1, 0, 1, 0, 0],
                 [1, 0, 1, 1, 1, 0, 1],
                 [0, 0, 0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0]], RepresentationType.ADJACENCY_MATRIX)
    groups = kosaraju(G)
    GraphPlotter.plot_graph(G, groups)
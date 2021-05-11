import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import GraphPlotter
from utils.graph_generators import randomize
from algorithms.euler import euler_cycle, generate_euler_graph_sequence


if __name__ == "__main__":
    randomizations = 100
    G = Graph()
    v = int(input('Number of vertices: '))
    
    if generate_euler_graph_sequence(G, v):
        print(G.repr)
    else:
        print("Error while generating euler graph sequence")
        exit()
        
    G.to_adjacency_matrix()
    randomize(G, randomizations)
    print(euler_cycle(G))
    GraphPlotter.plot_graph(G)
    
# minimal input: 3
# maximal input: 100-500 ~up to 62500 edges (without drawing)

import os, sys, copy

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import plot_graph
from utils.graph_generators import randomize
from algorithms.euler import euler_cycle, generate_euler_graph_sequence


if __name__ == "__main__":
    randomizations = 100
    G = Graph()
    v = int(input('Number of vertices: ')) # 10-50 should be fine
    
    while(True):
        if G.load_data(generate_euler_graph_sequence(v), RepresentationType.GRAPH_SEQUENCE):
            break

    print(G.repr)
    G.to_adjacency_matrix()

    randomize(G, randomizations)

    G.to_adjacency_list()
    print(euler_cycle(copy.deepcopy(G.repr)))
    G.to_adjacency_matrix()
    plot_graph(G)
    

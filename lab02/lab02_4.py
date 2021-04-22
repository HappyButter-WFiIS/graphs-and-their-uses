import os, sys, copy

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.GraphRepresentation import GraphRepresentation, RepresentationType
from utils.GraphPlotter import plot_graph
from algorithms.euler import euler_cycle, generate_euler_graph_sequence
from lab02_2 import randomize

randomizations = 100

if __name__ == "__main__":
    v = int(input('Number of vertices: ')) # 10-50 should be fine
    G = GraphRepresentation()
    while(True):
        if G.load_data(generate_euler_graph_sequence(v), RepresentationType.GRAPH_SEQUENCE):
            break

    print(G.repr)
    G.to_adjacency_matrix()

    for _ in range(randomizations):
        randomize(G)

    G.to_adjacency_list()
    print(euler_cycle(copy.deepcopy(G.repr)))
    G.to_adjacency_matrix()
    plot_graph(G.repr)
    

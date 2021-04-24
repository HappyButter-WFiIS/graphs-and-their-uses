import os, sys, copy

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.graph_generators import gen_random_conn_graph_weighted
from utils.GraphRepresentation import GraphRepresentation, RepresentationType
from utils.GraphPlotter import plot_graph

from algorithms.dijkstra import find_shortest_path


if __name__ == "__main__":
    random_conn_graph = gen_random_conn_graph_weighted(10)

    G = GraphRepresentation()
    G.load_data(data=random_conn_graph,
                representation_type=RepresentationType.ADJACENCY_MATRIX_WITH_WEIGHTS)
    print(G)
    plot_graph(G.repr)

    s = 1
    print(50*'-')
    print("START: s = {}".format(s))

    for i in range(10):
        find_shortest_path(G=G.get_weighted_adjacency_list(), start=s, destination=i+1)
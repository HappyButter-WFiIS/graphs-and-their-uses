import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_generators import gen_random_conn_graph_weighted
from utils.graph_plotter import GraphPlotter
from algorithms.dijkstra import find_shortest_path


if __name__ == "__main__":
    random_conn_graph = gen_random_conn_graph_weighted(12)

    G = Graph()
    G.load_data(data=random_conn_graph,
                representation_type=RepresentationType.ADJACENCY_MATRIX_WITH_WEIGHTS)
    print(G)
    GraphPlotter.plot_graph(G)

    s = 1
    print(50*'-')
    print("START: s = {0}".format(s))

    for i in range(10):
        find_shortest_path(G=G.get_weighted_adjacency_list(), start=s, destination=i+1)
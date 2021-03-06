import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_generators import gen_random_conn_graph_weighted

if __name__ == "__main__":
    random_conn_graph = gen_random_conn_graph_weighted(10)

    G = Graph()
    G.load_data(data=random_conn_graph,
                representation_type=RepresentationType.ADJACENCY_MATRIX_WITH_WEIGHTS)

    print(G.get_distance_matrix())

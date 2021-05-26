from algorithms.johnson import johnson_algorithm
from utils.graph_generators import get_connected_digraph

randomgraph = get_connected_digraph(10, 0.3, -2, 10)
randomgraph.to_adjacency_matrix()

johnson_algorithm(randomgraph)
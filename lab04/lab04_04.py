import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from algorithms.johnson import johnson_algorithm
from utils.graph_generators import get_connected_digraph

randomgraph = get_connected_digraph(10, 0.3, 2, 10)
randomgraph.to_adjacency_matrix()

johnson_algorithm(randomgraph)
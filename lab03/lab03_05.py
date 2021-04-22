
import os, sys, copy

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from lab03_01 import gen_random_conn_graph_weighted
from utils.GraphRepresentation import GraphRepresentation, RepresentationType
from utils.GraphPlotter import plot_graph
from algorithms.mst import kruskal, prim

if __name__ == '__main__':
    v = int(input('Number of vertices: ')) 
    G = GraphRepresentation()
    G.load_data(gen_random_conn_graph_weighted(v), RepresentationType.ADJACENCY_MATRIX)
    plot_graph(G.repr)
    MST = kruskal(G.repr)
    plot_graph(MST)
    MST = prim(G.repr)
    plot_graph(MST)

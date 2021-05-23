import os, sys, copy

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_generators import gen_random_conn_graph_weighted
from utils.graph_plotter import GraphPlotter
from algorithms.mst import kruskal, prim

if __name__ == '__main__':
    v = int(input('Number of vertices: '))
    G = Graph()
    G.load_data(gen_random_conn_graph_weighted(v), RepresentationType.ADJACENCY_MATRIX)
    GraphPlotter.plot_graph(G, draw_wages = True)
    MST = kruskal(G.repr)
    G.load_data(MST, RepresentationType.ADJACENCY_MATRIX)
    GraphPlotter.plot_graph(G, draw_wages = True)
    MST = prim(G.repr)
    G.load_data(MST, RepresentationType.ADJACENCY_MATRIX)
    GraphPlotter.plot_graph(G,  draw_wages = True)

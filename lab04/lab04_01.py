import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.graph_generators import get_directed_graph_with_probability, get_graph_with_probability

x = get_directed_graph_with_probability(10, 0.2)

for i in x:
    print(i)

from utils.graph_plotter import GraphPlotter
from utils.DirectedGraph import DirectedGraph, RepresentationType

g = DirectedGraph()
g.load_data(data=x, representation_type=RepresentationType.ADJACENCY_MATRIX)
GraphPlotter.plot_graph(g)

g.to_incidence_matrix()
g.to_adjacency_matrix()
g.to_adjacency_list()
g.to_adjacency_matrix()

g.to_adjacency_list()
g.to_incidence_matrix()
g.to_adjacency_list()
g.to_adjacency_matrix()

GraphPlotter.plot_graph(g)
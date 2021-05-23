import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.DirectedGraph import DirectedGraph, RepresentationType
from utils.graph_plotter import GraphPlotter
from algorithms.kosaraju import kosaraju
from algorithms.bellman_ford import bellman_ford
from utils.graph_generators import get_connected_digraph


if __name__ == '__main__':

	g = get_connected_digraph(5, 0.2, -5, 10)
	
	try: 
		start = 1
		print("\nShortest paths from node [{}]:".format(start))
		print(bellman_ford(g, start))
	except Exception as e:
		print(e)

	GraphPlotter.plot_graph(g)
    

import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.graph_generators import get_flow_network
from utils.FlowNetworkPlotter import FlowNetworkPlotter

graph1 = [[0, 16, 13,  0, 0,  0],
          [0,  0, 10, 12, 0,  0],
          [0,  4,  0,  0, 14, 0],
          [0,  0,  9,  0, 0, 20],
          [0,  0,  0,  7, 0,  4],
          [0,  0,  0,  0, 0,  0]]

# EXPECTED MAXIMUM FLOW IS 23

network = get_flow_network(n=2)
network.repr = graph1
network.source_node = 0
network.target_node = 5
print(network)
plotter = FlowNetworkPlotter()
plotter.load_network(network)
plotter.plot(rand_offset_factor=0.6)
print("Max flow: ")
print(network.ford_fulkerson(network.source_node, network.target_node)) #CAUTION! fold_fulkerson modifies original network
network.clear_flow_network()

import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.FlowNetwork import FlowNetwork
from utils.graph_generators import get_flow_network 
from utils.FlowNetworkPlotter import FlowNetworkPlotter

network = get_flow_network(n=4)
print(network)

plotter = FlowNetworkPlotter()
plotter.load_network(network)
plotter.plot()

network.clear_flow_network()

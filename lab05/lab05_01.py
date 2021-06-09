import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.graph_generators import get_flow_network 
from utils.FlowNetwork import FlowNetwork

network = get_flow_network(2)

print(network)
network.clear_flow_network()

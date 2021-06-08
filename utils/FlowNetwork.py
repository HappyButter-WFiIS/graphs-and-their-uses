from typing import overload
import numpy as np

from utils.DirectedGraph import DirectedGraph, RepresentationType

class FlowNetwork(DirectedGraph):
    
    layers = list()
     
    def load_flow_network(self, graph: list, layers: list) -> None:
        self.load_data(graph, RepresentationType.ADJACENCY_MATRIX)
        self.layers = layers
        
    def clear_flow_network(self):
        self.repr = list()
        self.repr_type = RepresentationType.EMPTY
        self.layers = list()
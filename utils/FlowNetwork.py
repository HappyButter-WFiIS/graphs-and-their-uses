from typing import overload
import numpy as np

from utils.DirectedGraph import DirectedGraph, RepresentationType


class FlowNetwork(DirectedGraph):
    
    layers = list()

    def __init__(self):
        super().__init__()
        self.source_node = -1
        self.target_node = -1

    def load_flow_network(self, graph: list, layers: list) -> None:
        self.load_data(graph, RepresentationType.ADJACENCY_MATRIX)
        self.layers = layers
        
    def clear_flow_network(self):
        self.repr = list()
        self.repr_type = RepresentationType.EMPTY
        self.layers = list()


    def breadth_first_search(self, s, t, parent):
        visited = [False] * (len(self.repr))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.repr[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (len(self.repr))
        max_flow = 0
        while self.breadth_first_search(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.repr[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while(v != source):
                u = parent[v]
                self.repr[u][v] -= path_flow
                self.repr[v][u] += path_flow
                v = parent[v]
        return max_flow

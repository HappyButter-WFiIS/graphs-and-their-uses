import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import plotly.graph_objs as go
import networkx as nx
from random import randint, random
from utils.AddEdge import add_edge
import numpy as np
from utils.FlowNetwork import FlowNetwork


class FlowNetworkPlotter:
    """
    Plots a FlowNetwork object in a friendly layered form.
    Each plotter remembers the last letwork loaded into it.
    """
    def __init__(self, node_size=30):
        self.node_size = node_size
        self.graph = None
        self.layers = None

    def load_network(self, network:FlowNetwork) -> None:
        """
        Loads a FlowNetwork object, so it could be plotted.
        """
        net = network
        net.to_adjacency_matrix()
        self.graph = net.repr
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if self.graph[i][j] is None:
                    self.graph[i][j] = 0
        self.layers = []
        cur_layer = 0
        for layer in net.layers:
            for node in layer:
                self.layers.append(cur_layer)
            cur_layer += 1

    def plot(self) -> None:
        """
        Opens an interactive plot in the default browser.
        """
        if self.graph is None or self.layers is None:
            raise Exception("Network not loaded")

        G = nx.convert_matrix.from_numpy_matrix(np.array(self.graph))
        node_x, node_y = self.__generate_node_positions(self.layers)

        node_trace = self.__plot_nodes(node_x, node_y)
        edge_trace = self.__plot_edges(G, node_x, node_y)
        text_trace = self.__plot_weights(G, self.graph, node_x, node_y)

        plot_data = []
        plot_data.append(edge_trace)
        plot_data.append(node_trace)
        plot_data.append(text_trace)
        
        node_adjacencies = []
        node_text = []
        for node, adjacencies in enumerate(G.adjacency()):
            layer = self.layers[node]
            if layer == min(self.layers):
                node_text.append(f'Source')
            elif layer == max(self.layers):
                node_text.append(f'Drain')
            else:
                node_text.append(f'Layer {layer}, node {node}')
            node_adjacencies.append(layer)
            

        node_trace.marker.color = node_adjacencies
        node_trace.text = node_text

        fig = go.Figure(
            data=plot_data,
            layout=go.Layout(
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
            )
        )
        fig.show()

    def __plot_edges(self, G, node_x, node_y):
        edge_x = []
        edge_y = []

        for edge in G.edges():
            if self.graph[edge[0]][edge[1]] == 0:
                edge = edge[1], edge[0]
            x0 = node_x[edge[0]]
            y0 = node_y[edge[0]]
            x1 = node_x[edge[1]]
            y1 = node_y[edge[1]]
            edge_x, edge_y = add_edge(
                start=(x0, y0), end=(x1, y1),
                edge_x=edge_x, edge_y=edge_y,
                lengthFrac=.95, arrowPos='end',
                arrowLength=.04,
                arrowAngle=30,
                dotSize=self.node_size
            )

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=1.5, color='#888'),
            hoverinfo='none',
            mode='lines'
        )
        return edge_trace

    def __plot_weights(self, G, graph, node_x, node_y):
        text_x = []
        text_y = []
        weights = []

        for edge in G.edges():
            if self.graph[edge[0]][edge[1]] == 0:
                edge = edge[1], edge[0]
            x0 = node_x[edge[0]]
            y0 = node_y[edge[0]]
            x1 = node_x[edge[1]]
            y1 = node_y[edge[1]]
            text_x.append((x1+x0)/2)
            text_y.append((y1+y0)/2)
            weights.append(graph[edge[0]][edge[1]])

        text_trace = go.Scatter(
            x=text_x, y=text_y,
            hoverinfo='none',
            text=weights,
            textposition='top center',
            textfont=dict(size=15),
            mode='text'
        )
        return text_trace

    def __plot_nodes(self, node_x, node_y):
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers', hoverinfo='text',
            marker=dict(
                showscale=False,
                colorscale='rainbow',
                reversescale=True,
                size=self.node_size,
                colorbar=dict(
                    thickness=30,
                    title='Flow capacity',
                    xanchor='left',
                    titleside='right'
                ),
                line_width=2
            )
        )
        return node_trace

    def __generate_node_positions(self, layers, rand_offset_factor=.4):

        def rand_offset():
            return (random() * randint(0,1) * rand_offset_factor)

        n = max(layers)
        num_of_nodes = len(layers)
        node_x = []
        node_y = []
        nodes_in_layer = [0] * (n+1)
        layer_counts = [0] * (n+1)

        for i in layers:
            nodes_in_layer[i] += 1

        for i in range(num_of_nodes):
            layer = layers[i]
            node_x.append(layer + rand_offset())
            node_y.append(layer_counts[layer] - (nodes_in_layer[layer] - 1) / 2 + rand_offset())
            layer_counts[layer] += 1

        return node_x, node_y

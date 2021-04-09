import os, sys
import numpy as np

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.GraphRepresentation import GraphRepresentation, RepresentationType
from utils.GraphPlotter import plot_graph

def randomize(G):
    edges = []
    for i in range(len(G.repr)):
        for j in range(i):
            if G.repr[i][j]:
                edges.append((i, j))

    first_edge = edges[np.random.randint(len(edges))]
    second_edge = edges[np.random.randint(len(edges))]

    a, b = first_edge
    c, d = second_edge

    if G.repr[a][d] or G.repr[c][b] or a == d or b == c:
        randomize(G)
    else:
        G.repr[a][b] = G.repr[b][a] = 0
        G.repr[c][d] = G.repr[d][c] = 0
        G.repr[a][d] = G.repr[d][a] = 1
        G.repr[c][b] = G.repr[b][c] = 1

if __name__ == "__main__":
    G = GraphRepresentation()
    G.load_data([4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2], RepresentationType.GRAPH_SEQUENCE)
    G.to_adjacency_matrix()

    plot_graph(G.repr)
    for _ in range(1000):
        randomize(G)
    plot_graph(G.repr)

import matplotlib.pyplot as plot
import numpy as np
from utils.Graph import RepresentationType, Graph

node_color_modes = [
    {'bg': 'blue', 'text': 'white'},
    {'bg': 'red', 'text': 'white'},
    {'bg': 'green', 'text': 'white'},
    {'bg': 'gray', 'text': 'white'},
    {'bg': 'pink', 'text': 'black'},
    {'bg': 'orange', 'text': 'black'},
    {'bg': 'purple', 'text': 'white'},
    {'bg': 'black', 'text': 'white'},
    {'bg': 'lightblue', 'text': 'black'},
    {'bg': 'brown', 'text': 'white'},
]


def plot_graph(G: Graph, groups: list = None):
    current_repr_type = G.repr_type
    if current_repr_type == RepresentationType.ADJACENCY_LIST \
            or current_repr_type == RepresentationType.ADJACENCY_MATRIX \
            or current_repr_type == RepresentationType.INCIDENCE_MATRIX \
            or current_repr_type == RepresentationType.GRAPH_SEQUENCE:
        G.to_adjacency_matrix()

        source_matrix = G.repr

        num_of_nodes = len(source_matrix)
        if groups is None:
            groups = [0] * num_of_nodes
        for i in range(len(groups)):
            if groups[i] > len(node_color_modes) - 1:
                groups[i] = 0
        ax = prepare_plot()
        draw_edges(num_of_nodes, source_matrix)
        draw_nodes(num_of_nodes, ax, groups)

        plot.show()
        if current_repr_type == RepresentationType.INCIDENCE_MATRIX:
            G.to_incidence_matrix()
        elif current_repr_type == RepresentationType.ADJACENCY_LIST:
            G.to_adjacency_list()

    else:
        print("Incorrect graph type.")


def prepare_plot():
    circle = plot.Circle((0, 0), 1, color='gray', fill=False,
                         linestyle="--", clip_on=False)
    fig, ax = plot.subplots()
    plot.axis('off')
    ax.add_patch(circle)
    ax.set_aspect('equal')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    return ax


def draw_nodes(num_of_nodes, ax, groups):
    for i in range(num_of_nodes):
        x = np.sin(2 * np.pi / num_of_nodes * i)
        y = np.cos(2 * np.pi / num_of_nodes * i)
        node = plot.Circle((x, y), 0.1, clip_on=False, zorder=3,
                           color=node_color_modes[groups[i]]["bg"])
        ax.annotate(str(i + 1), xy=(x, y), fontsize=15,
                    ha="center", va="center",
                    color=node_color_modes[groups[i]]["text"])
        ax.add_patch(node)


def draw_edges(num_of_nodes, source_matrix):
    for row in range(num_of_nodes):
        for col in range(row):
            if source_matrix[row][col] == 0:
                continue
            xx = [np.sin(2 * np.pi / num_of_nodes * col),
                  np.sin(2 * np.pi / num_of_nodes * row)]
            yy = [np.cos(2 * np.pi / num_of_nodes * col),
                  np.cos(2 * np.pi / num_of_nodes * row)]
            plot.plot(xx, yy, color="black")

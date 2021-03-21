import matplotlib.pyplot as plot
import numpy as np


def plot_graph(source_matrix):
    num_of_nodes = len(source_matrix)
    ax = prepare_plot()
    draw_edges(num_of_nodes, source_matrix)
    draw_nodes(num_of_nodes, ax)

    plot.show()


def prepare_plot():
    circle = plot.Circle((0, 0), 1, color='gray', fill=False, linestyle="--", clip_on=False)
    fig, ax = plot.subplots()
    plot.axis('off')
    ax.add_patch(circle)
    ax.set_aspect('equal')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    return ax


def draw_nodes(num_of_nodes, ax):
    for i in range(num_of_nodes):
        x = np.sin(2 * np.pi / num_of_nodes * i)
        y = np.cos(2 * np.pi / num_of_nodes * i)
        node = plot.Circle((x, y), 0.1, clip_on=False, zorder=3)
        ax.annotate(str(i + 1), xy=(x, y), fontsize=15, ha="center", va="center")
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

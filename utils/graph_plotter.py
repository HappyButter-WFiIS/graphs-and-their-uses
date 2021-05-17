import matplotlib.pyplot as plot
import numpy as np
import math
from utils.Graph import RepresentationType, Graph


class GraphPlotter:
    """
    List of color themes for available for a node. Can be modified.
    """
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

    """
    Plots graph using Matplotlib. If color modes are not passed, the color of each node will be the same.
    """
    @staticmethod
    def plot_graph(graph: Graph, nodes_color_modes: list = None) -> None:
        current_repr_type = graph.repr_type
        if current_repr_type == RepresentationType.ADJACENCY_LIST \
                or current_repr_type == RepresentationType.ADJACENCY_MATRIX \
                or current_repr_type == RepresentationType.INCIDENCE_MATRIX \
                or current_repr_type == RepresentationType.GRAPH_SEQUENCE:
            graph.to_adjacency_matrix()

            source_matrix = graph.repr

            num_of_nodes = len(source_matrix)
            if nodes_color_modes is None:
                nodes_color_modes = [0] * num_of_nodes
            for i in range(len(nodes_color_modes)):
                if nodes_color_modes[i] > len(GraphPlotter.node_color_modes) - 1:
                    nodes_color_modes[i] = 0
            ax = GraphPlotter.__prepare_plot()
            GraphPlotter.__draw_edges(num_of_nodes, source_matrix)
            GraphPlotter.__draw_nodes(num_of_nodes, ax, nodes_color_modes)

            plot.show()
            if current_repr_type == RepresentationType.INCIDENCE_MATRIX:
                graph.to_incidence_matrix()
            elif current_repr_type == RepresentationType.ADJACENCY_LIST:
                graph.to_adjacency_list()

        else:
            print("Incorrect graph type.")

    @staticmethod
    def __prepare_plot():
        circle = plot.Circle((0, 0), 1, color='gray', fill=False,
                             linestyle="--", clip_on=False)
        fig, ax = plot.subplots()
        plot.axis('off')
        ax.add_patch(circle)
        ax.set_aspect('equal')
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        return ax

    @staticmethod
    def __draw_nodes(num_of_nodes, ax, groups) -> None:
        for i in range(num_of_nodes):
            x = np.sin(2 * np.pi / num_of_nodes * i)
            y = np.cos(2 * np.pi / num_of_nodes * i)
            node = plot.Circle((x, y), 0.1, clip_on=False, zorder=3,
                               color=GraphPlotter.node_color_modes[groups[i]]["bg"])
            ax.annotate(str(i + 1), xy=(x, y), fontsize=15,
                        ha="center", va="center",
                        color=GraphPlotter.node_color_modes[groups[i]]["text"])
            ax.add_patch(node)

    @staticmethod
    def __draw_edges(num_of_nodes, source_matrix) -> None:
        pi = np.pi
        for row in range(num_of_nodes):
            for col in range(row):
                if row == col:
                    continue
                first_wage = source_matrix[row][col]
                second_wage = source_matrix[col][row]
                if first_wage == 0 and second_wage == 0:
                    continue
                xx = [np.sin(2 * pi / num_of_nodes * col),
                      np.sin(2 * pi / num_of_nodes * row)]
                yy = [np.cos(2 * pi / num_of_nodes * col),
                      np.cos(2 * pi / num_of_nodes * row)]
                plot.plot(xx, yy, color="black")

                offset = 6

                if first_wage != 0:
                    first_wage_x = (xx[1] - xx[0])
                    first_wage_y = (yy[1] - yy[0])
                    length = math.sqrt(first_wage_x ** 2 + first_wage_y ** 2)
                    first_wage_x /= length * offset
                    first_wage_y /= length * offset
                    first_wage_x += xx[0]
                    first_wage_y += yy[0]
                    t = plot.text(s=str(second_wage),
                                  x=first_wage_x,
                                  y=first_wage_y,
                                  fontsize=10,
                                  ha='center',
                                  va='center')
                    t.set_bbox(dict(pad=0.1, color='white'))

                if second_wage != 0:
                    second_wage_x = (xx[0] - xx[1])
                    second_wage_y = (yy[0] - yy[1])
                    length = math.sqrt(second_wage_x ** 2 + second_wage_y ** 2)
                    second_wage_x /= length * offset
                    second_wage_y /= length * offset
                    second_wage_x += xx[1]
                    second_wage_y += yy[1]
                    t = plot.text(s=str(second_wage),
                                  x=second_wage_x,
                                  y=second_wage_y,
                                  fontsize=10,
                                  ha='center',
                                  va='center')
                    t.set_bbox(dict(pad=0.1, color='white'))

import matplotlib.pyplot as plot
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
            node_positions = GraphPlotter.__get_node_positions(num_of_nodes)

            GraphPlotter.__draw_edges(num_of_nodes=num_of_nodes,
                                      source_matrix=source_matrix,
                                      node_positions=node_positions)

            GraphPlotter.__draw_wages(num_of_nodes=num_of_nodes,
                                      source_matrix=source_matrix,
                                      node_positions=node_positions)

            GraphPlotter.__draw_nodes(num_of_nodes=num_of_nodes,
                                      ax=ax,
                                      groups=nodes_color_modes,
                                      node_positions=node_positions)

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
    def __draw_nodes(num_of_nodes, ax, groups, node_positions) -> None:
        for i in range(num_of_nodes):

            node = plot.Circle((node_positions[i][0],
                                node_positions[i][1]),
                               0.1, clip_on=False, zorder=3,
                               color=GraphPlotter.node_color_modes[groups[i]]["bg"])
            ax.annotate(str(i + 1),
                        xy=(node_positions[i][0],
                            node_positions[i][1]),
                        fontsize=15,
                        ha="center", va="center",
                        color=GraphPlotter.node_color_modes[groups[i]]["text"])
            ax.add_patch(node)

    @staticmethod
    def __get_node_positions(num_of_nodes) -> list:
        pi = math.pi
        positions = []
        for node_idx in range(num_of_nodes):
            positions.append([math.sin(2 * pi / num_of_nodes * node_idx),
                              math.cos(2 * pi / num_of_nodes * node_idx)])
        return positions

    @staticmethod
    def __draw_edges(num_of_nodes, source_matrix, node_positions) -> None:
        pi = math.pi
        for row in range(num_of_nodes):
            for col in range(row):
                if row == col:
                    continue
                first_wage = source_matrix[row][col]
                second_wage = source_matrix[col][row]
                if first_wage == 0 and second_wage == 0:
                    continue
                xx = [node_positions[col][0],
                      node_positions[row][0]]
                yy = [node_positions[col][1],
                      node_positions[row][1]]
                plot.plot(xx, yy, color="black")

    @staticmethod
    def __draw_wages(num_of_nodes, source_matrix, node_positions) -> None:
        offset = 5
        pi = math.pi
        for row in range(num_of_nodes):
            for col in range(num_of_nodes):
                if row == col:
                    continue
                xx = [node_positions[col][0],
                      node_positions[row][0]]
                yy = [node_positions[col][1],
                      node_positions[row][1]]
                if source_matrix[row][col] != 0:
                    x = (xx[1] - xx[0])
                    y = (yy[1] - yy[0])
                    length = math.sqrt(x ** 2 + y ** 2)
                    x /= length * offset
                    y /= length * offset
                    x += xx[0]
                    y += yy[0]
                    t = plot.text(s=str(source_matrix[row][col]),
                                  x=x,
                                  y=y,
                                  fontsize=10,
                                  ha='center',
                                  va='center')
                    t.set_bbox(dict(pad=0.1, color='white'))